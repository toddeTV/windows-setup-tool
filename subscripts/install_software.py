from subscript_skeleton import SubscriptSkeleton
from utils.result_type import SubScriptResult


class InstallSoftware(SubscriptSkeleton):
    name_short = "install_software"  # max 30 chars
    name_long = "Install Software"

    def run(self) -> SubScriptResult:
        self.print("Do something.")
        return SubScriptResult.SUCCESS
