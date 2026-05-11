import json
import time

class ReplayEngine:
    def replay(self, filename="trace.json"):
        with open(filename, "r") as f:
            trace = json.load(f)

        print("\n=== Replaying Trace ===\n")

        for step in trace:
            print(f"ACTION: {step['action']}")
            print(f"STATE : {step['state']}")
            print("-" * 40)

            time.sleep(0.5)