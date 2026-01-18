from langgraph.graph import StateGraph, END
from core.state import DebateState
from agents.pro_agent import ProAgent
from agents.contra_agent import ContraAgent
from agents.judge_agent import JudgeAgent
from agents.critic_agent import CriticAgent
from controllers.round_controller import RoundController
from core.storage import DebateStorage

# Instantiate core components
pro_agent = ProAgent()
contra_agent = ContraAgent()
judge_agent = JudgeAgent()
critic_agent = CriticAgent()
controller = RoundController()
storage = DebateStorage()


# ---- Wrapper nodes (LangGraph nodes must be functions) ----

def pro_node(state: DebateState):
    result = pro_agent.run(state)
    controller.handle_pro_result(state, result)
    return state


def contra_node(state: DebateState):
    result = contra_agent.run(state)
    controller.handle_contra_result(state, result)
    return state


def judge_node(state: DebateState):
    result = judge_agent.run(state)
    controller.handle_judge_result(state, result)
    return state


def critic_node(state: DebateState):
    result = critic_agent.run(state)
    controller.handle_critic_result(state, result)
    return state


def save_node(state: DebateState):
    path = storage.save(state)
    print(f"\n📁 Debate saved to: {path}")
    return state


# ---- Conditional routing ----

def route_after_round(state: DebateState):
    """
    Decide whether to continue debate rounds or go to judge.
    """
    if controller.should_continue(state):
        controller.next_round(state)
        return "pro"
    return "judge"


# ---- Build Graph ----

def build_debate_graph():
    graph = StateGraph(DebateState)

    # Add nodes
    graph.add_node("pro", pro_node)
    graph.add_node("contra", contra_node)
    graph.add_node("judge", judge_node)
    graph.add_node("critic", critic_node)
    graph.add_node("save", save_node)

    # Entry point
    graph.set_entry_point("pro")

    # Debate round flow
    graph.add_edge("pro", "contra")

    # After Contra, decide: next round or judge
    graph.add_conditional_edges(
        "contra",
        route_after_round,
        {
            "pro": "pro",
            "judge": "judge"
        }
    )

    # Judge → Critic → Save → END
    graph.add_edge("judge", "critic")
    graph.add_edge("critic", "save")
    graph.add_edge("save", END)

    return graph.compile()
