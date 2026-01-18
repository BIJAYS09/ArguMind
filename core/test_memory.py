from core.memory import MemoryManager

state = {
    "topic": "Test",
    "round": 1,
    "max_rounds": 3,
    "pro_history": [],
    "contra_history": [],
    "scores": {},
    "verdict": "",
    "critic_review": ""
}

mem = MemoryManager()
mem.add_pro_argument(state, "Pro says yes")
mem.add_contra_argument(state, "Contra says no")
mem.update_scores(state, 7, 5)
mem.set_verdict(state, "Pro wins")
mem.increment_round(state)

print(state)
