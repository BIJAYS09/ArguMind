import json
from agents.base_agent import BaseAgent
from llm.llm_factory import get_llm
from core.state import DebateState

class JudgeAgent(BaseAgent):
    """
    Evaluates the entire debate, scores both sides,
    and declares a winner with reasoning.
    """

    def __init__(self):
        # Judge should be more deterministic
        super().__init__(get_llm(temperature=0.2))

    def run(self, state: DebateState) -> dict:
        topic = state["topic"]
        pro_history = state["pro_history"]
        contra_history = state["contra_history"]

        prompt = f"""
You are an impartial debate judge.

Topic: {topic}

Pro Arguments (all rounds):
{pro_history}

Contra Arguments (all rounds):
{contra_history}

Your task:
1. Score Pro and Contra from 0 to 10.
2. Decide the winner.
3. Explain briefly why.

Return ONLY valid JSON in this exact format:

{{
  "winner": "Pro or Contra",
  "pro_score": <number>,
  "contra_score": <number>,
  "reason": "short explanation"
}}
"""

        response = self.llm.invoke(prompt)
        text = response.content.strip()

        # Try to parse JSON safely
        try:
            result = json.loads(text)
        except json.JSONDecodeError:
            # Fallback if the model returns messy output
            result = {
                "winner": "Unknown",
                "pro_score": 0,
                "contra_score": 0,
                "reason": text
            }

        return {
            "judge_result": result
        }
