from subscript_skeleton import SubscriptSkeleton
from utils.result_type import SubScriptResult


class SetupSystemSettings(SubscriptSkeleton):
    name_short = "setup_system_settings"  # max 30 chars
    name_long = "Setup System Settings"

    def run(self) -> SubScriptResult:
        self.print("Do something.")

        try:
            user_input = input("Simulate failure? (yes/no/hard): ").lower()
            if user_input == "yes":
                print("Soft abort triggered.")
                return SubScriptResult.ABORT_SOFT
            elif user_input == "hard":
                print("Hard abort triggered.")
                return SubScriptResult.ABORT_HARD

            print("Successfully applied settings.")
            return SubScriptResult.SUCCESS

        except Exception as e:
            print(f"Exception: {str(e)}")
            return SubScriptResult.ABORT_SOFT
