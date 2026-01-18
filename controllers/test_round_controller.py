from controllers.round_controller import RoundController

state = {
    "topic": "Test",
    "round": 1,
    "max_rounds": 3,
    "pro_history": [],
    "contra_history": [],
    "scores": {},
    "verdict": "",
    "critic_review": ""
}

controller = RoundController()

print("Continue?", controller.should_continue(state))
controller.next_round(state)
print("Round:", state["round"])
