from collections import Counter

class TraceMetrics:
    def score(self, trace, failures):
        score = 100

        penalty_map = {
            "retry_loop": 20,
            "uncertain_fix": 10,
            "failing_tests": 25,
            "incomplete_fix": 15,
        }

        for failure in failures:
            score -= penalty_map.get(failure["type"], 5)

        return max(score, 0)

    def cluster_failures(self, failures):
        counts = Counter(f["type"] for f in failures)
        return dict(counts)

    def render_clusters(self, clusters):
        print("\n=== Failure Clusters ===")
        if not clusters:
            print("No clusters detected.")
            return

        for name, count in clusters.items():
            bar = "#" * count
            print(f"{name:16} {bar} ({count})")