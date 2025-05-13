from sys import exit as sysExit
from subscript_skeleton import SubscriptSkeleton
from utils.colors import (
    COLOR,
    colorize,
    init_colorama,
)
from utils.logs import Logs
from utils.pretty_err import init_pretty_errors
from utils.result_type import SubScriptResult
from traceback import print_exc
from subscripts.install_software import InstallSoftware
from subscripts.setup_system_settings import SetupSystemSettings
from random import choice


def main():
    """Main function as global program entry."""

    # There could be a global Exception catch here, but we want them to be thrown at this level. Only executing the
    # subscripts should be caught and handled.

    # sys.excepthook = custom_exception_hook_with_logger

    print_header()

    Logs().log_with_prefix_main()
    init_pretty_errors()
    init_colorama()

    run_all_sub_scripts()

    exit_program()


def print_header():
    line_length = 50
    Logs().log_with_prefix_main("=" * line_length)
    Logs().log_with_prefix_main("windows_setup_tool".center(line_length))
    Logs().log_with_prefix_main("Automated Computer Setup".center(line_length))
    Logs().log_with_prefix_main("=" * line_length)
    Logs().log_with_prefix_main()
    Logs().log_with_prefix_main("ℹ️ Information:")
    Logs().log_with_prefix_main(
        "   This tool helps system administrators quickly prepare new computers."
    )
    Logs().log_with_prefix_main("👋 Welcome to the setup tool!")


def run_all_sub_scripts():
    Logs().log_with_prefix_main()
    Logs().log_with_prefix_main("▶️  Running all sub-scripts...")

    possible_subscript_prefix_colors = [
        # COLOR.RESET_ALL, # no reset as it is no color
        COLOR.BLUE,
        COLOR.CYAN,
        COLOR.GREEN,
        # COLOR.MAGENTA, # only for main script
        # COLOR.RED, # only for errors
        COLOR.YELLOW,
    ]

    # Create a list of all subscript with a random color for each
    # TODO for a subscript do not use the same color as the last subscript
    subscripts: list[SubscriptSkeleton] = [
        SetupSystemSettings(prefix_color=choice(possible_subscript_prefix_colors)),
        InstallSoftware(prefix_color=choice(possible_subscript_prefix_colors)),
    ]

    for script_instance in subscripts:
        Logs().log_with_prefix_main()
        Logs().log_with_prefix_main(
            f"Running sub-script: '{script_instance.name_short}'"
        )
        script_instance.log("ℹ️ Now starting ...")
        result = safe_run_script(script_instance, script_instance.name_short)

        if result == SubScriptResult.SUCCESS:
            script_instance.log(colorize("✅ Success.", COLOR.GREEN))
            Logs().log_with_prefix_main("Continuing with next script.")
        elif result == SubScriptResult.ABORT_SOFT:
            script_instance.log(colorize("⚠️ Soft abort.", COLOR.YELLOW))
            Logs().log_with_prefix_main("Continuing with other scripts.")
        elif result == SubScriptResult.ABORT_HARD:
            script_instance.log(colorize("🛑 Hard abort.", COLOR.RED))
            Logs().log_with_prefix_main("Abort full program with all other scripts.")
            sysExit(2)
        elif result == SubScriptResult.ABORT_EXCEPTION:
            script_instance.log(colorize("❗ Exception occurred.", COLOR.RED))
            Logs().log_with_prefix_main(
                "Print exception and then continue with other scripts."
            )
            print_exc()
        elif result == SubScriptResult.ABORT_USER:
            Logs().log_with_prefix_main(
                "⚓ Program interrupted by user (Ctrl+C). Exiting gracefully..."
            )
            sysExit(1)


def safe_run_script(subscript: SubscriptSkeleton, script_name):
    try:
        result = subscript.run()
        if result not in (
            SubScriptResult.SUCCESS,
            SubScriptResult.ABORT_SOFT,
            SubScriptResult.ABORT_HARD,
            SubScriptResult.ABORT_EXCEPTION,
            SubScriptResult.ABORT_USER,
        ):
            Logs().log_with_prefix_main(
                f"⚠️ Unknown result '{result}' in subscript '{script_name}'. Treating as soft abort."
            )
            return SubScriptResult.ABORT_SOFT
        return result

    except KeyboardInterrupt:
        return SubScriptResult.ABORT_USER

    except Exception:
        return SubScriptResult.ABORT_EXCEPTION


def exit_program():
    Logs().log_with_prefix_main()
    Logs().log_with_prefix_main("👋 Goodbye!")
    sysExit(0)


if __name__ == "__main__":
    main()
