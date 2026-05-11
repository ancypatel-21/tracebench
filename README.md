# TraceBench

AI agent failure analysis and replay framework for debugging, evaluating, and benchmarking autonomous coding workflows.

---

## Overview

TraceBench is an execution-trace evaluation framework designed to analyze the behavior of AI coding agents across realistic software engineering tasks. The system records agent execution traces, replays decision workflows step-by-step, detects subtle failure modes, and generates structured evaluation metrics for debugging and reproducibility.

The framework simulates how frontier AI systems are evaluated internally by analyzing execution behavior rather than only final correctness. TraceBench focuses on identifying hidden reasoning failures such as retry loops, incomplete fixes, inconsistent execution flows, and faulty assumptions during multi-step problem solving.

---

## Key Capabilities

- Execution trace logging and replay  
- AI-agent workflow visualization  
- Failure detection across multi-step executions  
- Retry-loop and incomplete-fix analysis  
- Runtime scoring and evaluation metrics  
- Failure clustering and pattern analysis  
- Modular evaluation pipeline for extensibility  

---

## System Architecture

```text
Agent Execution
      ↓
Trace Logger
      ↓
Replay Engine
      ↓
Failure Detector
      ↓
Scoring + Cluster Analysis
      ↓
Evaluation Report
```

---

## Core Components

### 1. Trace Logger
`tracer.py` records execution steps including:
- actions taken by the agent
- execution state
- timestamps
- intermediate outputs

Each trace is serialized into structured JSON for reproducibility and replay.

---

### 2. Replay Engine
`replay.py` replays execution traces step-by-step to:
- reproduce workflows
- inspect execution order
- analyze debugging behavior
- visualize agent reasoning sequences

---

### 3. Failure Detection Engine
`detector.py` identifies hidden execution failures including:
- retry loops
- uncertain fixes
- incomplete resolutions
- failing test scenarios
- inconsistent execution flows

The detector evaluates execution behavior rather than only final outputs.

---

### 4. Failure Analysis Pipeline
`analyzer.py` aggregates recurring failure patterns across traces and groups them into clusters for evaluation.

Examples:
- runtime instability
- repeated retries
- incomplete reasoning
- invalid fixes

---

### 5. Metrics & Scoring
`metrics.py` computes:
- execution quality scores
- failure penalties
- cluster distributions
- workflow performance summaries

The framework supports extensible reward-style scoring for RL-based evaluation environments.

---

## Evaluation Workflow

1. An AI agent executes a coding task.
2. TraceBench logs every execution step.
3. The replay engine reconstructs the workflow.
4. Failure detectors identify problematic reasoning patterns.
5. Metrics compute evaluation scores.
6. Failure clusters summarize recurring weaknesses.

---

## Project Structure

```text
tracebench/
├── main.py
├── tracer.py
├── replay.py
├── detector.py
├── analyzer.py
├── metrics.py
├── trace.json
└── README.md
```

---

## Run the Project

```bash
python3 main.py
```

---

## Sample Output

```text
=== Replaying Trace ===

ACTION: retrieve_context
STATE : {'query': 'Fix API timeout issue'}

ACTION: generate_fix
STATE : {'code_patch': 'Increase retry timeout to 5s'}

ACTION: run_tests
STATE : {'tests_passed': False}

=== Failure Report ===
- Step 3: failing_tests -> Tests failed after applying the fix.
- Step 6: retry_loop -> Agent is stuck in a retry loop.

=== Trace Score ===
Score: 55/100

=== Failure Clusters ===
failing_tests   ## (2)
retry_loop      # (1)
```

---

## Tech Stack

- Python  
- Execution Tracing  
- Evaluation Pipelines  
- Failure Analysis  
- Runtime Scoring  
- Debugging & Replay Systems  

---

## Key Learnings

- Designing execution-trace evaluation systems  
- Building replayable debugging pipelines  
- Detecting hidden reasoning failures in AI agents  
- Structuring modular evaluation environments  
- Creating scoring systems for autonomous workflows  

---

## Why This Project Matters

Modern AI coding agents often fail in subtle ways that are difficult to identify using correctness-only benchmarks. TraceBench focuses on analyzing execution behavior itself, enabling:
- reproducible debugging
- workflow-level evaluation
- failure-pattern discovery
- agent reliability analysis

The framework reflects core ideas used in frontier AI evaluation infrastructure for coding agents and autonomous software systems.

---

## Future Improvements

- Parallel trace evaluation workers  
- Web dashboard for trace visualization  
- Multi-agent execution comparison  
- Docker sandbox execution  
- RL-style reward modeling  
- Integration with real LLM APIs  
- Long-horizon reasoning evaluation  

---

## Author

Ancy Patel