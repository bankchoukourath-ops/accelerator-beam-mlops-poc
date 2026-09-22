# MLOps and Deterministic Safety Gate for Particle Accelerators

A reference testbench illustrating how to deploy AI agents on critical control systems (EPICS) without risking hardware damage.

---

## Architecture Overview

```
[ AI Agent / LLM ]
        │
        ▼ (JSON-RPC)
[ MCP Gateway (Model Context Protocol) ]
        │
        ▼
┌────────────────────────────────────────┐
│  Deterministic Software Safety Gate    │
│  - Setpoint bounded: [30.0 A - 60.0 A] │
│  - Out-of-bounds fallback: 45.0 A      │
└────────────────────────────────────────┘
        │
        ▼ (Process Variables)
[ Simulated EPICS Control System / PVs ]
```

---

## Key Features

* **EPICS MCP Gateway:** Standardized tooling exposing read diagnostics and magnet setpoint controls.
* **Deterministic Safety Gate:** Enforces hardware boundaries at the software interface before reaching the machine.
* **Scientific FAIR Metadata:** `metadata_fair.jsonld` structured under Schema.org and QUDT ontologies for open-science reproducibility.
* **Statistical Data Drift:** Kolmogorov-Smirnov two-sample test monitoring beam intensity drift (p < 0.01 alert trigger).
* **HPC-Ready CI/CD:** GitLab CI pipeline covering linting, test suites, and rootless Apptainer image building.

---

## Quickstart

1. **Clone the repository:**
```bash
git clone [https://github.com/bankchoukourath-ops/accelerator-beam-mlops-poc.git](https://github.com/bankchoukourath-ops/accelerator-beam-mlops-poc.git)
cd accelerator-beam-mlops-poc
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the test suite:**
```bash
pytest
```

---

## License
Distributed under the Apache 2.0 License. See `LICENSE` for details.
