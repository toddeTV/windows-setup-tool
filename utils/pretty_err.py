from pretty_errors import configure, blacklist
from os import environ


def init_pretty_errors():
    """
    Initializes `pretty_errors` for cross-platform compatibility.
    This function should be called at the start of the program.
    """
    # Check if `pretty_errors` is already initialized & ensure it's only initialized once
    if not hasattr(init_pretty_errors, "initialized"):
        # Logs().log_with_prefix_main(
        #     log_level=LogLevelEnum.DEBUG, message="Initializing 'pretty_errors'."
        # )
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


# def custom_exception_hook_with_logger(exc_type, exc_value, tb):

#     local_vars = {}
#     while tb:
#         filename = tb.tb_frame.f_code.co_filename
#         name = tb.tb_frame.f_code.co_name
#         line_no = tb.tb_lineno
#         print(f"File {filename} line {line_no}, in {name}")

#         local_vars = tb.tb_frame.f_locals
#         tb = tb.tb_next
#     print(f"Local variables in top frame: {local_vars}")
