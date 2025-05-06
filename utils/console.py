import os
from colorama import init, Fore, Style
from enum import Enum


def init_colorama():
    """
    Initializes colorama for cross-platform compatibility.
    This function should be called at the start of the program to ensure
    that ANSI escape sequences are interpreted correctly on Windows.
    """
    # Check if colorama is already initialized & ensure it's only initialized once
    if not hasattr(init_colorama, "initialized"):
        print_with_prefix_main("Initializing 'colorama'.")
        init_colorama.initialized = True
        init(autoreset=True)
    else:
        # If already initialized, do nothing
        return


class COLOR(Enum):
    """
    Enum for color codes used in the console.
    """

    RESET_ALL = Style.RESET_ALL
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN  # good for input prompts
    GREEN = Fore.GREEN
    MAGENTA = Fore.MAGENTA
    RED = Fore.RED
    YELLOW = Fore.YELLOW


def colorize(text: str, color: COLOR) -> str:
    """
    Colorizes the given text with the specified color.
    Args:
        text (str): The text to colorize.
        color (COLOR): The color to apply.
    Returns:
        str: The colorized text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(color, COLOR):
        raise TypeError("color must be an instance of COLOR Enum")
    return f"{color.value}{text}{COLOR.RESET_ALL.value}"


def print_with_prefix(prefix: str, color: COLOR, *args, **kwargs):
    """Prints the message with the main identifier as prefix."""
    text: str = " ".join(map(str, args))
    if text == "":
        print()
        return
    prefix_modified: str = f"[{colorize(prefix.center(30), color)}] "
    print(f"{prefix_modified}{text}", **kwargs)


def print_with_prefix_main(*args, **kwargs):
    """Prints the message with the main identifier as prefix."""
    print_with_prefix("main", COLOR.MAGENTA, *args, **kwargs)
