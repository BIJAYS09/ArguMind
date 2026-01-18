import json
import os
from datetime import datetime
from core.state import DebateState

class DebateStorage:
    """
    Handles persistence of debate sessions.
    Currently uses JSON files, can be replaced by DB later.
    """

    def __init__(self, base_dir: str = "debate_history"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def save(self, state: DebateState) -> str:
        """
        Save the debate state to a JSON file.
        Returns the path of the saved file.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"debate_{timestamp}.json"
        path = os.path.join(self.base_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4, ensure_ascii=False)

        return path

    def load(self, path: str) -> DebateState:
        """
        Load a debate state from a JSON file.

        """
