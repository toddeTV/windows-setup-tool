import logging
import re
import os

from utils.colors import COLOR, colorize
from utils.singleton import Singleton
from datetime import datetime
from enum import Enum


class LogLevelEnum(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    # CRITICAL = logging.CRITICAL
    # FATAL = logging.FATAL


# from typing import Literal
# LogLevelType = Literal[LogLevelEnum.ERROR, LogLevelEnum.WARNING]


class NoColorFormatter(logging.Formatter):
    _ANSI_ESCAPE = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")

    def format(self, record):
        original_msg = record.msg
        # ANSI entfernen
        record.msg = self._ANSI_ESCAPE.sub("", str(record.msg))
        formatted = super().format(record)
        record.msg = original_msg  # restore original message
        return formatted


class Logs(metaclass=Singleton):
    """
    Singleton class for logging.
    This class is used to log messages to a file and the console.
    It ensures that only one instance of the logger is created and used throughout the application.
    """

    _log_path: str = "logs"
    _filename: str = datetime.today().strftime("%Y-%m-%d_%H-%M-%S.log")
    _full_path: str = f"{_log_path}/{_filename}"

    # Create the log directory if it doesn't exist
    os.makedirs(_log_path, exist_ok=True)

    # handler: file
    handler_file = logging.FileHandler(_full_path, mode="a", encoding="utf-8")
    # handler_file.setLevel(logging.DEBUG)
    handler_file.setFormatter(
        NoColorFormatter(  # remove colors when logging to file
            "%(asctime)-15s %(levelname)-8s %(message)s"
        )
    )

    # handler: console
    handler_console = logging.StreamHandler()
    # handler_console.setLevel(logging.DEBUG)
    handler_console.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))

    _logger_CUSTOM: logging.Logger = logging.getLogger("windows_setup_tool")
    _logger_CUSTOM.setLevel(logging.DEBUG)
    if not _logger_CUSTOM.handlers:
        _logger_CUSTOM.addHandler(handler_file)
        _logger_CUSTOM.addHandler(handler_console)
    # _logger_CUSTOM.propagate = False

    _logger_STDOUT: logging.Logger = logging.getLogger("STDOUT")
    _logger_STDERR: logging.Logger = logging.getLogger("STDERR")

    @property
    def logger_CUSTOM(self) -> logging.Logger:
        return self._logger_CUSTOM

    @property
    def logger_STDOUT(self) -> logging.Logger:
        return self._logger_STDOUT

    @property
    def logger_STDERR(self) -> logging.Logger:
        return self._logger_STDERR

    def log(self, message: str, level: LogLevelEnum = LogLevelEnum.DEBUG) -> None:
        """
        Logs a message with the specified log level.

        Args:
            message (str): The message to log.
            level (LogLevelEnum): The log level to use.

        Raises:
            TypeError: If level is not an instance of LogLevelEnum or message is not a string.
        """

        if not isinstance(message, str):
            raise TypeError(
                f"Expected 'message' to be str, got {type(message).__name__}"
            )
        if not isinstance(level, LogLevelEnum):
            raise TypeError(
                f"Expected 'level' to be LogLevelEnum, got {type(level).__name__}"
            )

        self.logger_CUSTOM.log(level.value, message)

    def log_with_prefix(
        self,
        prefix_text: str,
        message: str = "",
        prefix_color: COLOR | None = None,
        log_level: LogLevelEnum = LogLevelEnum.INFO,
    ) -> None:
        """
        Logs a message with a colored prefix block.

        Args:
            prefix_text (str): The label shown in brackets.
            message (str): The message to log.
            prefix_color (COLOR | None): Color for the prefix text.
            log_level (LogLevelEnum): Logging level.

        Raises:
            TypeError: If prefix_text is not a string or message is not a string.
        """

        if not isinstance(prefix_text, str):
            raise TypeError(
                f"'prefix_text' must be str, got {type(prefix_text).__name__}"
            )
        if not isinstance(message, str):
            raise TypeError(f"'message' must be str, got {type(message).__name__}")

        prefix_color = prefix_color or COLOR.RESET_ALL
        padded_prefix = prefix_text.ljust(30)
        prefix = f"[{colorize(padded_prefix, prefix_color)}]"

        full_message = f"{prefix} {message}".rstrip()
        self.log(full_message, level=log_level)

    def log_with_prefix_main(
        self, message: str = "", log_level: LogLevelEnum = LogLevelEnum.INFO
    ) -> None:
        """
        Shortcut to log a message with a 'main' prefix.

        Args:
            message (str): The message to log.
            log_level (LogLevelEnum): Logging level.
        """
        self.log_with_prefix(
            prefix_text="main",
            prefix_color=COLOR.MAGENTA,
            message=message,
            log_level=log_level,
        )
