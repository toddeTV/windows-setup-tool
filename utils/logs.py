import logging
import re

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

    # handler: file
    handler_file = logging.FileHandler(_full_path)
    handler_file.setLevel(logging.DEBUG)
    handler_file.setFormatter(
        NoColorFormatter(  # remove colors when logging to file
            "%(asctime)-15s %(levelname)-8s %(message)s"
        )
    )
    # handler_file.mode = "w"
    handler_file.mode = "a+"
    handler_file.encoding = "utf-8"

    # handler: console
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.DEBUG)
    handler_console.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))

    # basic logging configuration
    logging.basicConfig(
        handlers=[handler_file, handler_console],
    )

    _logger_CUSTOM: logging.Logger = logging.getLogger("windows_setup_tool")
    _logger_STDOUT: logging.Logger = logging.getLogger("STDOUT")
    _logger_STDERR: logging.Logger = logging.getLogger("STDERR")

    def log(self, message: str, level: LogLevelEnum = LogLevelEnum.DEBUG) -> None:
        """
        Logs a message with the specified log level.
        Args:
            level (LogLevelEnum): The log level to use.
            message (str): The message to log.
        """

        if not isinstance(level, LogLevelEnum):
            raise TypeError("level must be an instance of LogLevelEnum")
        if not isinstance(message, str):
            raise TypeError("message must be a string")

        self._logger_CUSTOM.log(level.value, message)

    def log_with_prefix(
        self,
        prefix_text: str,
        message: str = "",
        prefix_color: COLOR | None = None,
        log_level: LogLevelEnum = LogLevelEnum.INFO,
    ):
        if prefix_color is None:
            prefix_color = COLOR.RESET_ALL

        # prefix_text_stretched: str = prefix_text.center(30)
        prefix_text_stretched: str = prefix_text.ljust(30)

        prefix_modified: str = f"[{colorize(prefix_text_stretched, prefix_color)}] "

        output: str = f"{prefix_modified}{message}"

        self.log(message=output, level=log_level)

    def log_with_prefix_main(
        self, message: str = "", log_level: LogLevelEnum = LogLevelEnum.INFO
    ):
        self.log_with_prefix(
            prefix_text="main",
            prefix_color=COLOR.MAGENTA,
            message=message,
            log_level=log_level,
        )

    def getLoggerCustom(self) -> logging.Logger:
        """
        Returns the custom logger.
        Returns:
            logging.Logger: The custom logger.
        """
        return self._logger_CUSTOM

    def getLoggerStdout(self) -> logging.Logger:
        """
        Returns the stdout logger.
        Returns:
            logging.Logger: The stdout logger.
        """
        return self._logger_STDOUT

    def getLoggerStderr(self) -> logging.Logger:
        """
        Returns the stderr logger.
        Returns:
            logging.Logger: The stderr logger.
        """
        return self._logger_STDERR
