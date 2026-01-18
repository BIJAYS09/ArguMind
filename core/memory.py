from core.state import DebateState

class MemoryManager:
    """
    Handles all memory updates for the debate.
    Keeps agents simple and focused only on reasoning.
    """

    def add_pro_argument(self, state: DebateState, text: str):
        state["pro_history"].append(text)

    def add_contra_argument(self, state: DebateState, text: str):
        state["contra_history"].append(text)

    def update_scores(self, state: DebateState, pro_score: int, contra_score: int):
        state["scores"]["pro"] = pro_score
        state["scores"]["contra"] = contra_score

    def set_verdict(self, state: DebateState, verdict: str):
        state["verdict"] = verdict

    def set_critic_review(self, state: DebateState, review: str):
        state["critic_review"] = review

    def increment_round(self, state: DebateState):
        state["round"] += 1
