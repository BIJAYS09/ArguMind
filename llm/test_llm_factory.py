from llm.llm_factory import get_llm

llm = get_llm()
res = llm.invoke("Say hello in one sentence.")
print(res.content)
