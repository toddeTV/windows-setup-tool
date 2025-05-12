import logging

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


class Logs(metaclass=Singleton):
    """
    Singleton class for logging.
    This class is used to log messages to a file and the console.
    It ensures that only one instance of the logger is created and used throughout the application.
    """

    _log_path: str = "logs"
    _filename: str = datetime.today().strftime("%Y-%m-%d_%H-%M-%S.log")
    _full_path: str = f"{_log_path}/{_filename}"

    logging.basicConfig(
        level=logging.DEBUG,
        filename=_full_path,
        filemode="a+",
        # filemode="w",
        encoding="utf-8",
        format="%(asctime)-15s %(levelname)-8s %(message)s",
    )

    _logger: logging.Logger = logging.getLogger()

    def log(self, level: LogLevelEnum, message: str) -> None:
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

        self._logger.log(level.value, message)

    def getLogger(self, name: str) -> logging.Logger:
        """
        Returns a logger with the specified name.
        Args:
            name (str): The name of the logger.
        Returns:
            logging.Logger: The logger with the specified name.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        return logging.getLogger(name)
