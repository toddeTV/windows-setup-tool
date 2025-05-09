from pretty_errors import configure, blacklist
from os import environ
from utils.console import print_with_prefix_main


def init_pretty_errors():
    """
    Initializes `pretty_errors` for cross-platform compatibility.
    This function should be called at the start of the program.
    """
    # Check if `pretty_errors` is already initialized & ensure it's only initialized once
    if not hasattr(init_pretty_errors, "initialized"):
        print_with_prefix_main("Initializing 'pretty_errors'.")
        init_pretty_errors.initialized = True
        configure(
            # separator_character="*",
            # filename_display=pretty_errors.FILENAME_EXTENDED,
            # line_number_first=True,
            # display_link=True,
            # lines_before=5,
            # lines_after=2,
            # line_color=pretty_errors.RED + "> " + pretty_errors.default_config.line_color,
            # code_color="  " + pretty_errors.default_config.line_color,
            # truncate_code=True,
            # display_locals=True,
        )
        blacklist(
            environ[
                "VIRTUAL_ENV"  # path to tne venv folder, e.g. `C:\foo\bar\windows_setup_tool\.venv`
            ]
        )
    else:
        # If already initialized, do nothing
        return
