from subscript_skeleton import SubscriptSkeleton
from utils.console import printf
from utils.result_type import SubScriptResult


class SetupSystemSettings(SubscriptSkeleton):
    name = "Setup System Settings"

    def run(self) -> SubScriptResult:
        prefix = f"[{self.name}]"
        printf("{prefix} Starting setup...")

        try:
            user_input = input(f"{prefix} Simulate failure? (yes/no/hard): ").lower()
            if user_input == "yes":
                printf("{prefix} Soft abort triggered.")
                return SubScriptResult.ABORT_SOFT
            elif user_input == "hard":
                printf("{prefix} Hard abort triggered.")
                return SubScriptResult.ABORT_HARD

            printf("{prefix} Successfully applied settings.")
            return SubScriptResult.SUCCESS

        except Exception as e:
            printf("{prefix} Exception: {str(e)}")
            return SubScriptResult.ABORT_SOFT
