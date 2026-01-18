from agents.base_agent import BaseAgent
from llm.llm_factory import get_llm
from core.state import DebateState

class ContraAgent(BaseAgent):
    """
    Argues against the topic.
    """

    def __init__(self):
        # Slightly creative but focused on critique
        super().__init__(get_llm(temperature=0.7))

    def run(self, state: DebateState) -> dict:
        round_no = state["round"]
        topic = state["topic"]

        last_pro = (
            state["pro_history"][-1]
            if state["pro_history"]
            else "No pro argument yet."
        )

        prompt = f"""
You are the CONTRA debater in a formal debate.

Topic: {topic}
Current Round: {round_no}

Last Pro Argument:
{last_pro}

Your task:
- Argue strongly against the topic.
- Point out flaws, risks, or weaknesses in the pro argument.
- Be logical, critical, and persuasive.
- Limit to 150–200 words.
"""

        response = self.llm.invoke(prompt)

        # Do not touch state directly, only return update
        return {
            "contra_argument": response.content
        }
