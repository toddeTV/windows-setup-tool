from colorama import init, Fore, Style
from enum import Enum
from utils.logs import LogLevelEnum, Logs


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


def init_colorama():
    """
    Initializes `colorama` for cross-platform compatibility.
    This function should be called at the start of the program to ensure
    that ANSI escape sequences are interpreted correctly on Windows.
    """
    # Check if `colorama` is already initialized & ensure it's only initialized once
    if not hasattr(init_colorama, "initialized"):
        print_with_prefix_main(
            log_level=LogLevelEnum.DEBUG, text="Initializing 'colorama'."
        )
        init_colorama.initialized = True
        init(autoreset=True)
    else:
        # If already initialized, do nothing
        return


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


# def print_with_prefix(prefix_text: str, prefix_color: COLOR, *args, **kwargs):
#     text: str = " ".join(map(str, args))
#     print(text, **kwargs)
def print_with_prefix(
    prefix_text: str,
    prefix_color: COLOR,
    text: str = "",
    log_level: LogLevelEnum = LogLevelEnum.INFO,
):
    """Prints the message with the main identifier as prefix."""

    if text == "":
        print()
        Logs().log(level=log_level, message="")
        return

    # prefix_text_stretched: str = prefix_text.center(30)
    prefix_text_stretched: str = prefix_text.ljust(30)

    prefix_modified_color_yes: str = (
        f"[{colorize(prefix_text_stretched, prefix_color)}] "
    )
    prefix_modified_color_no: str = f"[{prefix_text_stretched}] "

    output_color_yes: str = f"{prefix_modified_color_yes}{text}"
    output_color_no: str = f"{prefix_modified_color_no}{text}"

    print(output_color_yes)
    Logs().log(level=log_level, message=output_color_no)


def print_with_prefix_main(text: str = "", log_level: LogLevelEnum = LogLevelEnum.INFO):
    """Prints the message with the main identifier as prefix."""
    print_with_prefix(
        prefix_text="main", prefix_color=COLOR.MAGENTA, text=text, log_level=log_level
    )
