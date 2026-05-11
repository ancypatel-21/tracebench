class FailureDetector:
    def detect(self, trace):
        failures = []

        retry_count = 0
        saw_failed_tests = False
        saw_fix_after_failure = False

        for i, step in enumerate(trace):
            action = step["action"]
            state = step["state"]

            if action == "retry_fix":
                retry_count += 1
                if retry_count >= 2:
                    failures.append({
                        "type": "retry_loop",
                        "step": i + 1,
                        "message": "Agent is stuck in a retry loop."
                    })

            if action == "generate_fix":
                code_patch = state.get("code_patch", "")
                if "maybe" in code_patch.lower() or "not sure" in code_patch.lower():
                    failures.append({
                        "type": "uncertain_fix",
                        "step": i + 1,
                        "message": "Generated fix is uncertain or under-specified."
                    })

                if saw_failed_tests:
                    saw_fix_after_failure = True

            if action == "run_tests":
                if state.get("tests_passed") is False:
                    saw_failed_tests = True
                    failures.append({
                        "type": "failing_tests",
                        "step": i + 1,
                        "message": "Tests failed after applying the fix."
                    })

            if action == "final_answer" and saw_failed_tests and not saw_fix_after_failure:
                failures.append({
                    "type": "incomplete_fix",
                    "step": i + 1,
                    "message": "Agent failed to produce a proper follow-up fix after test failure."
                })

        return failures