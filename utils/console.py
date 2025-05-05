from colorama import init, Fore, Style
from enum import Enum


# Initialize colorama
init()


class COLOR_ENUM(Enum):
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    RESET_ALL = Style.RESET_ALL


def printf(text: str):
    print(f"{text}")


def printc(text: str, color: COLOR_ENUM):
    print(f"{get_colored(text, color)}")


def get_colored(text: str, color: COLOR_ENUM) -> str:
    return f"{color}{text}{COLOR_ENUM.RESET_ALL}"


def ask_input(prompt: str) -> str:
    return input(f"{COLOR_ENUM.CYAN}{prompt}{COLOR_ENUM.RESET_ALL}")
