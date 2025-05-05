from subscript_skeleton import SubscriptSkeleton
from utils.console import printf
from utils.result_type import SubScriptResult


class InstallSoftware(SubscriptSkeleton):
    name = "Install Software"

    def run(self) -> SubScriptResult:
        prefix = f"[{self.name}]"
        printf("{prefix} Starting software installation...")

        printf("{prefix} Installed all required programs successfully.")

        return SubScriptResult.SUCCESS
