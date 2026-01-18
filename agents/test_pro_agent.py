from agents.pro_agent import ProAgent

state = {
    "topic": "AI should replace human teachers",
    "round": 1,
    "max_rounds": 3,
    "pro_history": [],
    "contra_history": [],
    "scores": {},
    "verdict": "",
    "critic_review": ""
}

agent = ProAgent()
result = agent.run(state)

print(result["pro_argument"])
