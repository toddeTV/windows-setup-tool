from utils.console import printf
from utils.pretty_errors import init_pretty_errors
from sys import exit as sysExit, executable
from traceback import print_exc
from subscripts.install_software import InstallSoftware
from subscripts.setup_system_settings import SetupSystemSettings
from utils.result_type import SubScriptResult


def main():
    """Main function as global program entry."""

    # There could be a global Exception catch here, but we want them to be thrown at this level. Only executing the
    # subscripts should be caught and handled.

    init_pretty_errors()
    print_header()
    run_all_sub_scripts()
    exit_program()


def print_header():
    line_length = 50
    printf("=" * line_length)
    printf("windows_setup_tool".center(line_length))
    printf("Automated Computer Setup".center(line_length))
    printf("=" * line_length)
    printf("\nℹ️ Information:")
    printf("   This tool helps system administrators quickly prepare new computers.")


def run_all_sub_scripts():
    printf("\n▶️  Running all sub-scripts...\n")

    subscripts = {
        SetupSystemSettings().name: SetupSystemSettings(),
        InstallSoftware().name: InstallSoftware(),
    }

    for script_name in list(subscripts.keys()):
        script_instance = subscripts[script_name]
        result = safe_run_script(script_instance.run, script_name)

        if result == SubScriptResult.ABORT_HARD:
            printf("🛑 Hard abort from {script_name}. Exiting program.")
            sysExit(2)


def safe_run_script(func, script_name):
    try:
        result = func()
        if result not in (
            SubScriptResult.SUCCESS,
            SubScriptResult.ABORT_SOFT,
            SubScriptResult.ABORT_HARD,
        ):
            printf(
                "⚠️  {script_name}: Unknown result '{result}'. Treating as soft abort."
            )
            return SubScriptResult.ABORT_SOFT
        return result

    except KeyboardInterrupt:
        printf("\n\n⚠️  Program interrupted by user (Ctrl+C). Exiting gracefully...")
        sysExit(1)

    except Exception:
        printf("❗ Exception occurred while running {script_name}:")
        print_exc()
        return SubScriptResult.ABORT_SOFT


def exit_program():
    printf("\n👋 Goodbye!")
    sysExit(0)


if __name__ == "__main__":
    main()
