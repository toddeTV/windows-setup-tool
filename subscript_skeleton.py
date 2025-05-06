from abc import ABC, abstractmethod
from utils.console import COLOR, colorize, print_with_prefix
from utils.result_type import SubScriptResult


class SubscriptSkeleton(ABC):
    """Base class for all sub-scripts."""

    # set in subscript classes
    name_short: str  # max 30 chars
    name_long: str

    # only stored, do not set in subscript classes
    prefix_name_color: COLOR

    def __init__(self, prefix_color: COLOR):
        """
        Initializes the sub-script with a color for the prefix and implementation checks/tests.
        """
        if not hasattr(self, "name_short"):
            raise ValueError("Sub-scripts must define a 'name_short' attribute.")
        if not self.name_short:
            raise ValueError("name_short must not be empty")
        if len(self.name_short) > 30:
            raise ValueError("name_short must be 30 characters or less")

        if not hasattr(self, "name_long"):
            raise ValueError("Sub-scripts must define a 'name_long' attribute.")
        if not self.name_long:
            raise ValueError("name_long must not be empty")

        if self.name_short == self.name_long:
            raise ValueError("name_short and name_long must be different")

        if not isinstance(prefix_color, COLOR):
            raise TypeError("prefix_color must be an instance of COLOR Enum")

        self.prefix_name_color = prefix_color

    def print(self, *args, **kwargs):
        """Prints the message with the sub-script name as prefix."""
        print_with_prefix(self.name_short, self.prefix_name_color, *args, **kwargs)

    @abstractmethod
    def run(self) -> SubScriptResult:
        """Each sub-script must implement the run method."""
        pass
