from collections import Counter

class FailureAnalyzer:
    def analyze(self, failures):
        if not failures:
            return {
                "total_failures": 0,
                "clusters": {},
                "summary": "No failures detected."
            }

        cluster_counts = Counter(f["type"] for f in failures)

        return {
            "total_failures": len(failures),
            "clusters": dict(cluster_counts),
            "summary": f"Detected {len(failures)} failures across {len(cluster_counts)} failure types."
        }