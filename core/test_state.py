from core.state import DebateState

state: DebateState = {
    "topic": "AI should replace human teachers",
    "round": 1,
    "max_rounds": 3,
    "pro_history": [],
    "contra_history": [],
    "scores": {},
    "verdict": "",
    "critic_review": ""
}

print(state)
