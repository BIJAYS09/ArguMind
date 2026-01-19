from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph.debate_graph import build_debate_graph
from core.state import DebateState

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DebateRequest(BaseModel):
    topic: str
    rounds: int = 3


@app.post("/run")
def run_debate(req: DebateRequest):
    app_graph = build_debate_graph()

    initial_state: DebateState = {
        "topic": req.topic,
        "round": 1,
        "max_rounds": req.rounds,
        "pro_history": [],
        "contra_history": [],
        "scores": {},
        "verdict": "",
        "critic_review": ""
    }

    final_state = app_graph.invoke(initial_state)
    return final_state
