from agents.base_agent import BaseAgent

class FakeLLM:
    def invoke(self, prompt):
        class Res:
            content = "Fake response"
        return Res()

class TestAgent(BaseAgent):
    def run(self, state):
        res = self.llm.invoke("test")
        return {"result": res.content}

agent = TestAgent(FakeLLM())
print(agent.run({}))
