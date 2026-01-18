from core.state import DebateState
from core.memory import MemoryManager

class RoundController:
    """
    Controls the debate loop:
    - Tracks rounds
    - Decides when to stop debating
    - Applies memory updates
    """

    def __init__(self):
        self.memory = MemoryManager()

    def handle_pro_result(self, state: DebateState, result: dict):
        """
        Store Pro agent output into memory.
        """
        pro_text = result.get("pro_argument", "")
        self.memory.add_pro_argument(state, pro_text)

    def handle_contra_result(self, state: DebateState, result: dict):
        """
        Store Contra agent output into memory.
        """
        contra_text = result.get("contra_argument", "")
        self.memory.add_contra_argument(state, contra_text)

    def handle_judge_result(self, state: DebateState, result: dict):
        """
        Store Judge decision into state.
        """
        judge = result.get("judge_result", {})

        state["scores"]["pro"] = judge.get("pro_score", 0)
        state["scores"]["contra"] = judge.get("contra_score", 0)

        state["verdict"] = (
            f"Winner: {judge.get('winner')} | Reason: {judge.get('reason')}"
        )

    def handle_critic_result(self, state: DebateState, result: dict):
        """
        Store Critic review.
        """
        state["critic_review"] = result.get("critic_review", "")

    def should_continue(self, state: DebateState) -> bool:
        """
        Decide whether another debate round is needed.
        """
        return state["round"] < state["max_rounds"]

    def next_round(self, state: DebateState):
        """
        Move to next round.
        """
        self.memory.increment_round(state)
