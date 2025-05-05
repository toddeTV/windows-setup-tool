from abc import ABC, abstractmethod
from utils.result_type import SubScriptResult


class SubscriptSkeleton(ABC):
    """Base class for all sub-scripts."""

    name: str

    def __init__(self):
        if not hasattr(self, "name"):
            raise ValueError("Sub-scripts must define a 'name' attribute.")

    @abstractmethod
    def run(self) -> SubScriptResult:
        """Each sub-script must implement the run method."""
        pass
