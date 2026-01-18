from abc import ABC, abstractmethod
from core.state import DebateState

class Agent(ABC):
    """
    Base interface for all agents in the debate system.
    Every agent must implement the run() method.
    """

    @abstractmethod
    def run(self, state: DebateState) -> dict:
        """
        Takes the current DebateState and returns
        a dictionary with updates to the state.
        """
        pass
