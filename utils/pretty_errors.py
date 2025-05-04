from pretty_errors import configure, blacklist
from os import environ


def init_pretty_errors():
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
    print()
    blacklist(
        environ[
            "VIRTUAL_ENV"  # path to tne venv folder, e.g. `C:\foo\bar\windows_setup_tool\.venv`
        ]
    )
