# FlowGentic–IMPRESS Hybrid Agent
### Autonomous Multi-Stage Protein Analysis Pipelines on HPC (Phase 2 Complete)

This repository contains the Phase 1–2 implementation of an autonomous workflow execution system integrating:

- **IMPRESS** (Radical-Cybertools) for HPC pipeline orchestration  
- **Radical AsyncFlow** for asynchronous execution  
- A modular **agent architecture** for planning and running computational biology workflows  
- A **workspace system** for reproducible results  
- A foundation for **LLM-driven workflow construction** (Phase 3)

This system is designed for fully automated, multi-step structural bioinformatics analysis on ACCESS HPC systems such as **Anvil**.

---

## 1. Project Summary

The goal of this project is to build an intelligent workflow agent capable of:

- Interpreting natural-language scientific requests  
- Constructing multi-step analysis pipelines  
- Executing these pipelines on HPC infrastructure using IMPRESS  
- Saving and returning structured results  
- Progressively learning from examples through few-shot prompting and fine-tuning  

Phase 2 (current release) implements:

- IMPRESS execution  
- AsyncFlow backend  
- Automated workspace creation  
- Pipeline definition and execution flow  
- Stub tool interface for future AlphaFold2, FoldSeek, ΔΔG, and MPNN integrations  

---

## 2. Repository Structure

```
flowgentic_agent/
│
├── agent_core/
│   ├── executor.py
│   ├── simple_pipeline.py
│   ├── workspace.py
│   ├── planner.py
│   ├── llm_planner.py          # (Phase 3) LLM-driven planner (coming soon)
│   ├── models.py
│
├── tools/
│   ├── alphafold_stub.py
│   ├── foldseek_stub.py
│   ├── ddg_stub.py
│   ├── mpnn_stub.py
│
├── configs/
│   ├── impress.yml
│   ├── flowgentic.yml
│
├── jobs_example/
│
├── legacy/
│   ├── run_phase1.py
│
├── run_phase2.py
├── README.md
├── requirements.txt
└── .gitignore
```

Temporary directories such as `agent_workspace/`, `outputs/`, and `logs/` are intentionally excluded from version control.

---

## 3. Phase 2 Functionality

### 3.1 IMPRESS Execution

The Phase 2 flow:

1. User input → `run_phase2.py`  
2. Workspace automatically created  
3. Executor initializes RadicalExecutionBackend  
4. IMPRESS Manager starts pipeline  
5. `SimplePipeline` executes a placeholder computation  
6. Results saved to `workspace/results/output.json`  
7. Executor loads JSON and returns final output  

This provides a fully functional backbone independent of heavy computational tools.

---

## 4. Tool Implementations (Stubs)

The `tools/` directory contains placeholders for future integration:

- AlphaFold2  
- FoldSeek  
- ΔΔG mutation scoring  
- Protein MPNN  

Currently, these files contain **stub functions**, used for:

- Pipeline flow testing  
- IMPRESS backend validation  
- Workspace I/O patterns  
- LLM-planning prototyping  

Actual tool integrations will be implemented in Phases 3–4.

---

## 5. Phase 3: LLM Workflow Planning (Upcoming)

Phase 3 introduces the **LLM-driven planner**, which will:

- Parse natural language queries  
- Generate structured workflow specifications  
- Map those to IMPRESS PipelineSetup definitions  
- Support conditional and multi-stage workflows  

Planned output example:

```json
{
  "stages": [
    {"stage": "AF2", "tool": "alphafold", "params": {"fasta": "<seq>"}},
    {"stage": "FOLDSEEK", "tool": "foldseek", "depends_on": "AF2"},
    {"stage": "DDG", "tool": "ddg_mutation", "depends_on": "AF2"}
  ]
}
```

We will begin by constructing *few-shot examples*, then creating a dataset for training a specialized planning model.

---

## 6. Running on ACCESS: Anvil

Start an interactive session:

```
sinteractive -A nairr240405-gpu -p gpu --gres=gpu:1 -N 1 -t 00:30:00
module load miniforge3
conda activate impress
```

Run the agent:

```
python run_phase2.py
```

---

## 7. Roadmap

### Phase 1  
Initial architecture + rule-based planning (completed)

### Phase 2  
Full IMPRESS + AsyncFlow integration  
Pipeline demonstration  
Workspace system  
Tool stubs (completed)

### Phase 3  
LLM workflow planner  
Few-shot dataset  
JSON workflow specification  
Tool schema integration (in progress)

### Phase 4  
Real AlphaFold2 + FoldSeek + ΔΔG + MPNN execution  
Adaptive pipelines  
Expanded tooling

### Phase 5  
Web UI (Streamlit)  
Provenance tracking  
Continuous learning  

---

## 8. Contributions

Contributions are welcome in:

- HPC/IMPRESS integration  
- Structural bioinformatics tooling  
- Machine learning workflow planning  
- Dataset construction  
- Software engineering and orchestration  

---

