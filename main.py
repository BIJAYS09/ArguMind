from graph.debate_graph import build_debate_graph
from core.state import DebateState

def create_initial_state(topic: str, max_rounds: int = 3) -> DebateState:
    return {
        "topic": topic,
        "round": 1,
        "max_rounds": max_rounds,
        "pro_history": [],
        "contra_history": [],
        "scores": {},
        "verdict": "",
        "critic_review": ""
    }

def pretty_print_results(state: DebateState):
    print("\n" + "=" * 60)
    print("🧩 MULTI-AGENT DEBATE SYSTEM RESULTS")
    print("=" * 60)

    print(f"\n📌 Topic: {state['topic']}")
    print(f"🔁 Rounds: {state['max_rounds']}")

    print("\n🟢 PRO ARGUMENTS:")
    for i, arg in enumerate(state["pro_history"], 1):
        print(f"\nRound {i}:\n{arg}")

    print("\n🔴 CONTRA ARGUMENTS:")
    for i, arg in enumerate(state["contra_history"], 1):
        print(f"\nRound {i}:\n{arg}")

    print("\n⚖ JUDGE VERDICT:")
    print(state["verdict"])

    print("\n📊 SCORES:")
    print(state["scores"])

    print("\n🧪 CRITIC REVIEW:")
    print(state["critic_review"])

    print("\n" + "=" * 60)

if __name__ == "__main__":
    print("🧠 Welcome to the Multi-Agent Debate System\n")

    topic = input("Enter a debate topic: ")
    rounds = input("How many rounds? (default = 3): ")

    max_rounds = int(rounds) if rounds.strip().isdigit() else 3

    initial_state = create_initial_state(topic, max_rounds)

    app = build_debate_graph()

    final_state = app.invoke(initial_state)

    pretty_print_results(final_state)
