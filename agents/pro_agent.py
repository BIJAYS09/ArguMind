from agents.base_agent import BaseAgent
from llm.llm_factory import get_llm
from core.state import DebateState

class ProAgent(BaseAgent):
    """
    Argues in favor of the topic.
    """

    def __init__(self):
        # Pro agent is creative, so a slightly higher temperature
        super().__init__(get_llm(temperature=0.7))

    def run(self, state: DebateState) -> dict:
        round_no = state["round"]
        topic = state["topic"]

        last_contra = (
            state["contra_history"][-1]
            if state["contra_history"]
            else "No contra argument yet."
        )

        prompt = f"""
You are the PRO debater in a formal debate.

Topic: {topic}
Current Round: {round_no}

Last Contra Argument:
{last_contra}

Your task:
- Argue strongly in favor of the topic.
- Be logical, concise, and persuasive.
- Respond to the contra argument if it exists.
- Limit to 150–200 words.
"""

        response = self.llm.invoke(prompt)

        # IMPORTANT:
        # We do NOT modify state here.
        # We only return what should be added.
        return {
            "pro_argument": response.content
        }
