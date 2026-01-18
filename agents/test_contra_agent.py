from agents.contra_agent import ContraAgent

state = {
    "topic": "AI should replace human teachers",
    "round": 1,
    "max_rounds": 3,
    "pro_history": ["AI can scale education cheaply and consistently."],
    "contra_history": [],
    "scores": {},
    "verdict": "",
    "critic_review": ""
}

agent = ContraAgent()
result = agent.run(state)

print(result["contra_argument"])
