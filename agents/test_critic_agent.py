from agents.critic_agent import CriticAgent

state = {
    "topic": "AI should replace human teachers",
    "round": 3,
    "max_rounds": 3,
    "pro_history": [
        "AI can scale education cheaply.",
        "AI personalizes learning.",
        "AI increases access globally."
    ],
    "contra_history": [
        "Teachers provide emotional support.",
        "AI lacks empathy.",
        "Human judgment is essential."
    ],
    "scores": {"pro": 8, "contra": 7},
    "verdict": "Pro wins because scalability and cost efficiency outweigh emotional aspects.",
    "critic_review": ""
}

agent = CriticAgent()
result = agent.run(state)

print(result["critic_review"])
