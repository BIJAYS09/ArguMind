from core.storage import DebateStorage

state = {
    "topic": "AI vs Humans",
    "round": 3,
    "max_rounds": 3,
    "pro_history": ["Pro arg 1", "Pro arg 2"],
    "contra_history": ["Contra arg 1", "Contra arg 2"],
    "scores": {"pro": 8, "contra": 6},
    "verdict": "Pro wins",
    "critic_review": "Balanced but Pro had stronger evidence"
}

storage = DebateStorage()
path = storage.save(state)
print("Saved to:", path)

loaded = storage.load(path)
print("Loaded:", loaded)
