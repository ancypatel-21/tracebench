from tracer import TraceLogger
from replay import ReplayEngine
from detector import FailureDetector
from analyzer import FailureAnalyzer
from metrics import TraceMetrics
import json

logger = TraceLogger()

# Simulated AI agent execution trace
logger.log_step("retrieve_context", {"query": "Fix API timeout issue"})
logger.log_step("generate_fix", {"code_patch": "Increase retry timeout to 5s"})
logger.log_step("run_tests", {"tests_passed": False})
logger.log_step("retry_fix", {"attempt": 2})
logger.log_step("generate_fix", {"code_patch": "Maybe increase timeout and adjust retry logic"})
logger.log_step("run_tests", {"tests_passed": False})
logger.log_step("retry_fix", {"attempt": 3})
logger.log_step("final_answer", {"status": "incomplete"})

logger.save()

with open("trace.json", "r") as f:
    trace = json.load(f)

replay = ReplayEngine()
replay.replay()

detector = FailureDetector()
failures = detector.detect(trace)

analyzer = FailureAnalyzer()
report = analyzer.analyze(failures)

metrics = TraceMetrics()
score = metrics.score(trace, failures)
clusters = metrics.cluster_failures(failures)

print("\n=== Failure Report ===")
for failure in failures:
    print(f"- Step {failure['step']}: {failure['type']} -> {failure['message']}")

print("\n=== Analysis Summary ===")
print(report["summary"])
print("Clusters:", report["clusters"])

print("\n=== Trace Score ===")
print(f"Score: {score}/100")

metrics.render_clusters(clusters)