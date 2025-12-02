FlowGentic–IMPRESS Hybrid Agent
Autonomous Multi-Stage Protein Analysis Pipelines on HPC (Phase 2 Complete)

This repository contains the Phase 1–2 implementation of an autonomous workflow execution system integrating:

- IMPRESS (Radical-Cybertools) for HPC pipeline orchestration

- Radical AsyncFlow for asynchronous execution

- A modular agent architecture for planning and running computational biology workflows

- A workspace system for reproducible results

- A foundation for LLM-driven workflow construction (Phase 3)

This system is designed for fully automated, multi-step structural bioinformatics analysis on ACCESS HPC systems such as Anvil.

1. Project Summary

The goal of this project is to build an intelligent workflow agent capable of:

Interpreting natural-language scientific requests

Constructing multi-step analysis pipelines

Executing these pipelines on HPC infrastructure via IMPRESS

Saving and returning structured results for downstream interpretation

Eventually learning to generalize through few-shot examples and dataset-driven fine-tuning

Phase 2 (current release) implements:

IMPRESS execution

AsyncFlow backend

Automated workspace creation

Pipeline definition and execution flow

Stub tool interface for future AlphaFold2, FoldSeek, ΔΔG, and MPNN integrations

2. Repository Structure
flowgentic_agent/
│
├── agent_core/
│   ├── executor.py          # IMPRESS execution wrapper
│   ├── simple_pipeline.py   # Phase 2 demonstration pipeline
│   ├── workspace.py         # Workspace manager
│   ├── planner.py           # Early rule-based planner
│   ├── llm_planner.py       # (Phase 3) LLM-driven planner (coming)
│   ├── models.py
│
├── tools/                   # Tool stubs (placeholders)
│   ├── alphafold_stub.py
│   ├── foldseek_stub.py
│   ├── ddg_stub.py
│   ├── mpnn_stub.py
│
├── configs/                 # YAML configuration files
│   ├── impress.yml
│   ├── flowgentic.yml
│
├── jobs_example/            # Example IMPRESS/SLURM job scripts (few-shot data)
│
├── legacy/                  # Phase 1 reference implementation
│   ├── run_phase1.py
│
├── run_phase2.py            # Main Phase 2 entrypoint
├── README.md
├── requirements.txt
└── .gitignore


Directories such as agent_workspace/, outputs/, and logs/ are runtime-only and ignored by Git.

3. Phase 2 Functionality
3.1 IMPRESS Execution Workflow

Phase 2 provides a complete execution flow:

User input → run_phase2.py

Workspace created automatically

Executor initializes RadicalExecutionBackend

IMPRESS Manager starts pipeline

SimplePipeline executes (placeholder logic)

Results written to workspace/results/output.json

Executor loads JSON and returns final output

This enables full backend testing without requiring heavy computational tools.

3.2 Workspace System

Each run produces an isolated directory:

agent_workspace/Q_<timestamp>/
    input/
    logs/
    intermediate/
    results/


The pipeline is responsible for writing a final output.json file.

3.3 Current Simple Pipeline

The demonstration pipeline:

Accepts FASTA

Simulates AF2/FoldSeek/DDG computations via stubs

Writes structured results into the workspace

Returns them to the user

This provides the foundation for real downstream tool integrations in Phase 3–4.

4. Tools: Current Status (Stubs Only)

The real computational tools are not yet implemented. The following files are placeholders:

alphafold_stub.py

foldseek_stub.py

ddg_stub.py

mpnn_stub.py

They currently emulate tool behavior for:

Pipeline testing

IMPRESS integration

Workspace I/O validation

LLM planning prototyping

Actual AlphaFold2, FoldSeek, ΔΔG, and MPNN pipelines will be implemented in Phase 3/4.

5. Phase 3: LLM-Driven Workflow Planning (Upcoming)

Phase 3 introduces an intelligent LLM-driven planner that will:

Parse natural language requests

Construct a structured multi-step workflow graph

Map each step to IMPRESS PipelineSetup objects

Handle dependencies (e.g., FoldSeek requires AF2 output)

Generate workflows such as:

Example:

{
  "stages": [
    {"stage": "AF2", "tool": "alphafold", "params": {"fasta": "<seq>"}},
    {"stage": "FOLDSEEK", "tool": "foldseek", "depends_on": "AF2"},
    {"stage": "DDG", "tool": "ddg_mutation", "depends_on": "AF2"}
  ]
}


We will begin with few-shot engineered examples, followed by dataset creation and eventual fine-tuning.

6. Running on ACCESS: Anvil

Start interactive session:

sinteractive -A nairr240405-gpu -p gpu --gres=gpu:1 -N 1 -t 00:30:00
module load miniforge3
conda activate impress


Run the agent:

python run_phase2.py

7. Roadmap
Phase 1

Rule-based planning prototype (completed)

Phase 2

IMPRESS + AsyncFlow execution
Workspace system
Tool interface (stubs)
Demonstration pipeline
(Completed)

Phase 3

LLM planner
Workflow graph generation
Few-shot dataset construction
Real tool interface definitions

Phase 4

Full integration of AF2, FoldSeek, ΔΔG, MPNN
Adaptive pipelines
Performance tuning on HPC

Phase 5

Web interface (Streamlit)
Provenance database
Continuous learning
Production-grade automation

8. Contributions

This project welcomes contributions in:

HPC orchestration

IMPRESS/AsyncFlow

Structural bioinformatics

LLM planning and dataset creation

Tool integration (AF2, FoldSeek, DDG, MPNN)

Software engineering and pipeline design
