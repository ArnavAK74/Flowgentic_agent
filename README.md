FlowGentic–IMPRESS Hybrid Agent
Autonomous Multi-Stage Protein Analysis Workflows on HPC (Phase 2 Completed)

This repository contains the Phase 1–2 implementation of an autonomous HPC workflow agent built on:

IMPRESS (Radical-Cybertools) for distributed workflow execution

Radical AsyncFlow as the asynchronous execution backend

FlowGentic-style workflow generation

HPC resources (ACCESS: Anvil)

A Python-based agent core for orchestration, planning, and workspace management

Phase 2 is fully functional: the agent can execute IMPRESS pipelines end-to-end, write results to workspace directories, and return structured outputs.

We now begin Phase 3: LLM-driven multi-step pipeline planning and, later, fine-tuning with custom datasets.

Project Overview

The agent is designed to translate natural language scientific queries into structured, multi-step computational workflows involving structural biology tools such as:

AlphaFold2 (AF2)

FoldSeek

ΔΔG mutation scoring

Protein MPNN sequence design

CAZy / UniProt annotation tools

While these real tools are not yet integrated (see the section below), the architecture is ready to support them.

Tool Implementations (Currently Stubs)

The tools/ directory contains placeholder stubs:

tools/
├── alphafold_stub.py
├── foldseek_stub.py
├── ddg_stub.py
├── mpnn_stub.py


These do not execute real AF2, FoldSeek, DDG, or MPNN workloads yet.
They are included so the pipeline planner, executor, and IMPRESS backend can be developed and tested independently from heavy computational components.

Real tool integrations (future phases)
Tool	Status	Notes
AlphaFold2 (AF2_GPU)	Not implemented	Will run via /projects/f_sdk94_1/Tools/AF2_GPU
FoldSeek	Not implemented	CPU/cluster pipeline; depends on AF2 output
ΔΔG (mutation prediction)	Not implemented	Sequence + structure-based ΔΔG scoring
Protein MPNN	Not implemented	Will support structure-conditioned sequence redesign

These will be integrated during Phase 3–4 after the LLM-based planner is operational.

Phase 2 Capabilities
IMPRESS Integration

Manager-based workflow execution

Automatic pipeline orchestration

WorkflowEngine initialized with backend

RadicalExecutionBackend functional on Anvil

Workspace Management

Workspaces are created for each request:

agent_workspace/Q_<timestamp>/
    input/
    logs/
    results/
    intermediate/

Successful End-to-End Execution

SimpleProteinPipeline:

Receives FASTA + workspace from executor

Runs under IMPRESS

Saves results/output.json

Executor loads this JSON and returns it as the final output

Phase 3: LLM-Driven Workflow Planning (In Progress)

Phase 3 introduces an LLM-based planner (llm_planner.py) that:

Reads natural-language queries

Generates a structured multi-step workflow plan (JSON)

Converts each stage into IMPRESS PipelineSetup objects

Executes them sequentially or conditionally (depending on results)

Enables adaptive, intelligent workflows for protein analysis

Example of desired LLM output format
{
  "stages": [
    {"stage": "AF2", "tool": "alphafold", "params": {"fasta": "<FASTA>"}},
    {"stage": "FOLDSEEK", "tool": "foldseek", "depends_on": "AF2"},
    {"stage": "DDG", "tool": "ddg_mutation", "depends_on": "AF2"}
  ]
}


The planner will initially use few-shot prompt engineering, followed by building a dataset for LoRA fine-tuning.

Repository Structure
flowgentic_agent/
│
├── agent_core/
│   ├── executor.py
│   ├── simple_pipeline.py
│   ├── workspace.py
│   ├── planner.py            # Earlier rule-based version
│   ├── llm_planner.py        # Phase 3 (to be added)
│   ├── models.py
│
├── tools/                    # Stubs only (real tools come later)
│   ├── alphafold_stub.py
│   ├── foldseek_stub.py
│   ├── ddg_stub.py
│   ├── mpnn_stub.py
│
├── configs/
│   ├── impress.yml
│   ├── flowgentic.yml
│
├── jobs_example/             # Example HPC job scripts for LLM training
│
├── run_phase2.py             # Main entrypoint for Phase 2
├── run_phase1.py             # Legacy version
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── agent_workspace/          # Runtime scratch (ignored)
├── logs/                     # Ignored
├── outputs/                  # Ignored
└── tmp/                      # Ignored

Running on Anvil

Start interactive session:

sinteractive -A nairr240405-gpu -p gpu --gres=gpu:1 -N 1 -t 00:30:00
module load miniforge3
conda activate impress


Run the agent:

python run_phase2.py

Roadmap
Phase 3 (current)

LLM planner

Workflow graph generation

Mapping plans to IMPRESS pipelines

Few-shot dataset

tool → pipeline schema

Phase 4

Real AlphaFold2 integration

FoldSeek pipeline

ΔΔG scoring

MPNN sequence design

Multi-stage workflow execution

Phase 5

Streamlit interface

Provenance tracking

Continuous learning

Advanced replanning with IMPRESS adaptive functions

Contributions

Collaborators are welcome to work on:

LLM-based planning

IMPRESS pipelines

tool integration

SLURM/HPC optimization

dataset generation

model finetuning
