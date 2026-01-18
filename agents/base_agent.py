from core.interfaces import Agent
from core.state import DebateState

class BaseAgent(Agent):
    """
    Base class for all debate agents.
    Implements shared functionality and stores the LLM.
    """

    def __init__(self, llm):
        self.llm = llm

    def run(self, state: DebateState) -> dict:
        """
        This should be overridden by child agents.
        """
        raise NotImplementedError("Subclasses must implement the run() method.")
