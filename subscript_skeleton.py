from abc import ABC, abstractmethod
from utils.console import COLOR, colorize, print_with_prefix
from utils.result_type import SubScriptResult


class SubscriptSkeleton(ABC):
    """Base class for all sub-scripts."""

    name_short: str  # max 30 chars
    name_long: str
    prefix_name_color: COLOR

    def __init__(self, prefix_color: COLOR):
        if not hasattr(self, "name_short"):
            raise ValueError("Sub-scripts must define a 'name_short' attribute.")
        if not hasattr(self, "name_long"):
            raise ValueError("Sub-scripts must define a 'name_long' attribute.")

        self.prefix_name_color = prefix_color

    def print(self, *args, **kwargs):
        """Prints the message with the sub-script name as prefix."""
        print_with_prefix(self.name_short, self.prefix_name_color, *args, **kwargs)

    @abstractmethod
    def run(self) -> SubScriptResult:
        """Each sub-script must implement the run method."""
        pass
