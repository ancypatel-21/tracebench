import json
import time

class TraceLogger:
    def __init__(self):
        self.trace = []

    def log_step(self, action, state):
        self.trace.append({
            "timestamp": time.time(),
            "action": action,
            "state": state
        })

    def save(self, filename="trace.json"):
        with open(filename, "w") as f:
            json.dump(self.trace, f, indent=2)

        print(f"Trace saved to {filename}")