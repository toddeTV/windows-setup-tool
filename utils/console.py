from colorama import init, Fore, Style
from enum import Enum


# Initialize colorama
init()


class COLOR(Enum):
    RESET_ALL = Style.RESET_ALL
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN  # good for input prompts


def colorize(text: str, color: COLOR) -> str:
    return f"{color}{text}{COLOR.RESET_ALL}"
