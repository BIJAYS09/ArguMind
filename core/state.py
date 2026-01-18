from typing import TypedDict, List, Dict

class DebateState(TypedDict):
    # Debate configuration
    topic: str
    round: int
    max_rounds: int

    # Memory
    pro_history: List[str]
    contra_history: List[str]

    # Scoring + decisions
    scores: Dict[str, int]
    verdict: str
    critic_review: str
