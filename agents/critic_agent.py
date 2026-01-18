from agents.base_agent import BaseAgent
from llm.llm_factory import get_llm
from core.state import DebateState

class CriticAgent(BaseAgent):
    """
    Reviews the judge's verdict for bias, logic errors, or weak reasoning.
    Acts as a quality control agent.
    """

    def __init__(self):
        # Low temperature for analytical behavior
        super().__init__(get_llm(temperature=0.2))

    def run(self, state: DebateState) -> dict:
        topic = state["topic"]
        pro_history = state["pro_history"]
        contra_history = state["contra_history"]
        verdict = state["verdict"]
        scores = state["scores"]

        prompt = f"""
You are a debate critic and auditor.

Topic: {topic}

Pro Arguments:
{pro_history}

Contra Arguments:
{contra_history}

Judge Verdict:
{verdict}

Scores:
{scores}

Your task:
- Check if the judge was biased.
- Check if important arguments were ignored.
- Check if the reasoning is logically sound.
- Suggest improvements if any.

Write a concise review (5–7 lines).
"""

        response = self.llm.invoke(prompt)

        return {
            "critic_review": response.content
        }
