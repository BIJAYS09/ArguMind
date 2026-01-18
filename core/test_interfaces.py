from core.interfaces import Agent
from core.state import DebateState

class DummyAgent(Agent):
    def run(self, state: DebateState) -> dict:
        return {"test": "ok"}

state = {
    "topic": "Test",
    "round": 1,
    "max_rounds": 1,
    "pro_history": [],
    "contra_history": [],
    "scores": {},
    "verdict": "",
    "critic_review": ""
}

agent = DummyAgent()
print(agent.run(state))
