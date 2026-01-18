from agents.judge_agent import JudgeAgent

state = {
    "topic": "AI should replace human teachers",
    "round": 3,
    "max_rounds": 3,
    "pro_history": [
        "AI provides scalable education.",
        "AI can personalize learning.",
        "AI reduces costs and increases access."
    ],
    "contra_history": [
        "Teachers provide emotional support.",
        "AI lacks human judgment.",
        "Education is more than information delivery."
    ],
    "scores": {},
    "verdict": "",
    "critic_review": ""
}

agent = JudgeAgent()
result = agent.run(state)

print(result["judge_result"])
