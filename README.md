# 🚀 Anvīkṣa Sanket AI
### Air-Gapped Predictive Copilot for Secure MPLS & SD-WAN Operations

> **Bharatiya Antariksh Hackathon 2026**
>
> **Problem Statement 13 – Air-Gapped Predictive Copilot for Secure MPLS Operations**

---

# 📖 Project Name Meaning

### **Anvīkṣa (अन्वीक्षा)**

Derived from the Sanskrit word **"Anvīkṣikī"**, meaning:

- Deep Investigation
- Analytical Reasoning
- Scientific Observation
- Intelligent Analysis

### **Sanket (संकेत)**

Derived from Hindi/Sanskrit, meaning:

- Early Signal
- Warning
- Indication
- Alert

### **Together**

**Anvīkṣa Sanket AI** means:

> **"An intelligent AI system that deeply analyzes secure network telemetry, predicts failures before they occur, provides early warning signals, explains the reasons behind elevated risk, and recommends preventive actions—all within a completely air-gapped environment."**

---

# 🎯 Project Overview

Anvīkṣa Sanket AI is an **offline AI-powered Network Operations Center (NOC) Copilot** designed for mission-critical MPLS and SD-WAN networks operating in secure environments.

Unlike traditional monitoring systems that react only after failures occur, this platform continuously analyzes network telemetry, predicts future network degradation, estimates the remaining time before SLA impact, explains the root cause, and recommends corrective actions.

The solution is specifically designed for organizations where cloud-based AI cannot be used, such as:

- ISRO
- Defence Networks
- Government Organizations
- Railways
- Banking Infrastructure
- Critical Industrial Networks

---

# ❓ Problem Statement

Current NOC tools answer:

> **"What has already failed?"**

Anvīkṣa Sanket AI answers:

✅ What will fail next?

✅ When will it fail?

✅ Why is the network at risk?

✅ What should the operator do before the failure occurs?

---

# 🎯 Current Repository Scope (MVP)

This repository currently implements the **Predictive Fault Analytics Engine**, which demonstrates:

- Synthetic telemetry generation
- Time-series forecasting
- Link utilization prediction
- SLA breach prediction
- Time-to-impact estimation
- Confidence interval generation
- Structured prediction alerts
- Forecast visualization

---

# 🏗️ Current Architecture

```text
                 Synthetic Telemetry
                         │
                         ▼
              Telemetry Generator
          generate_telemetry.py
                         │
                    telemetry.csv
                         │
                         ▼
            Predictive Forecast Engine
             forecast_engine.py
                         │
                    forecast.csv
                         │
                         ▼
          Time-to-Impact Calculator
              impact_calc.py
                         │
            prediction_alert.json
                         │
                         ▼
            Visualization Generator
             output_generator.py
                         │
              forecast_chart.png
```

---

# 📁 Project Structure

```
Anviksha-Sanket-AI/

│
├── generate_telemetry.py
├── forecast_engine.py
├── impact_calc.py
├── output_generator.py
├── run_pipeline.py
│
├── data/
│     telemetry.csv
│
├── output/
│     forecast.csv
│     prediction_alert.json
│     forecast_chart.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<username>/Anviksha-Sanket-AI.git

cd Anviksha-Sanket-AI
```

Install all required packages

```bash
python -m pip install -r requirements.txt
```

---

# ▶️ Run the Complete Project

Execute the complete prediction pipeline

```bash
python run_pipeline.py
```

---

# ▶️ Run Individual Modules

Generate synthetic telemetry

```bash
python generate_telemetry.py
```

Run forecasting model

```bash
python forecast_engine.py
```

Estimate time-to-impact

```bash
python impact_calc.py
```

Generate visualization

```bash
python output_generator.py
```

---

# 📊 Output Files

| File | Description |
|------|-------------|
| telemetry.csv | Synthetic network telemetry |
| forecast.csv | Forecasted utilization values |
| prediction_alert.json | Structured AI prediction alert |
| forecast_chart.png | Historical vs Forecast visualization |

---

# ✨ Current Features

- Synthetic telemetry generator
- Prophet time-series forecasting
- SLA threshold prediction
- Time-to-impact estimation
- Confidence interval prediction
- Automated prediction alerts
- Forecast visualization

---

# 🛣️ Development Roadmap

## ✅ Milestone 1 — Predictive Fault Analytics Engine *(Completed)*

Implemented:

- Synthetic telemetry generation
- Time-series forecasting
- SLA breach prediction
- Time-to-impact estimation
- JSON alert generation
- Forecast visualization

---

## 🚧 Milestone 2 — SD-WAN/MPLS Network Simulation

Planned:

- Multi-site topology
- MPLS forwarding
- VPN segmentation
- IPSec tunnels
- BGP
- OSPF
- QoS
- Traffic generation
- Fault injection

---

## 🚧 Milestone 3 — Advanced Predictive Analytics

Upcoming:

- Latency prediction
- Packet loss prediction
- Jitter forecasting
- Tunnel health prediction
- CPU & Memory prediction
- BGP route flap prediction
- OSPF convergence prediction
- Network Risk Score

---

## 🚧 Milestone 4 — Offline AI Copilot

Planned:

- Offline LLM
- Natural language queries
- Root cause explanation
- AI-generated incident summaries
- Preventive recommendations

Models:

- Phi-3 Mini
- Mistral 7B
- Llama 3

---

## 🚧 Milestone 5 — Local RAG

Knowledge Sources:

- Network topology
- Device inventory
- Incident history
- Operational runbooks
- Alert history

Technologies:

- FAISS
- ChromaDB

---

## 🚧 Milestone 6 — Interactive Dashboard

Features:

- Network topology visualization
- Risk gauge
- Forecast charts
- Incident timeline
- AI Copilot chat
- Recommended actions

Frameworks:

- Streamlit
- Grafana
- FastAPI

---

## 🚧 Milestone 7 — Workflow Automation

Future Features:

- Alert prioritization
- Event correlation
- Automated playbooks
- Operator guidance
- SLA impact estimation

---

## 🚧 Milestone 8 — Scenario Validation

Planned Test Scenarios:

- Progressive congestion
- MPLS underlay failure
- Tunnel degradation
- Packet loss escalation
- BGP route flapping
- Controller policy drift
- QoS misconfiguration

Evaluation Metrics:

- Prediction accuracy
- Lead time
- Precision
- Recall
- False-positive rate
- Copilot response quality

---

# 💻 Technologies Used

### Programming

- Python 3.10+

### Machine Learning

- Prophet
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

### Future Technologies

- LSTM
- XGBoost
- TensorFlow
- PyTorch
- Ollama
- Phi-3 Mini
- Mistral 7B
- FAISS
- Streamlit
- FastAPI
- Prometheus
- Grafana
- Containerlab
- EVE-NG

---

# 📋 Alignment with Hackathon Objectives

| Objective | Status |
|-----------|--------|
| Simulated SD-WAN/MPLS Environment | 🚧 Planned |
| Predictive Fault Analytics Engine | ✅ Completed (MVP) |
| Offline LLM Copilot | 🚧 Planned |
| Workflow Automation | 🚧 Planned |
| Air-Gapped Deployment | 🚧 Planned |
| Scenario Validation | 🚧 Planned |

---

# 📈 Project Progress

```
████████████░░░░░░░░░░░░░░░░

Overall Progress

≈ 40%
```

---

# 🔮 Future Vision

Anvīkṣa Sanket AI will evolve into a **fully autonomous Air-Gapped AI Network Operations Center Copilot** capable of predicting failures hours in advance, explaining network behavior through offline AI, and assisting operators with intelligent preventive actions.

The completed platform will integrate:

- SD-WAN/MPLS Digital Twin
- Multi-metric Predictive Analytics
- Offline Large Language Model
- Retrieval-Augmented Generation (RAG)
- Intelligent Workflow Automation
- Interactive AI Dashboard

to provide a complete offline AI solution for mission-critical secure networks.

---
# 📄 License

Developed as part of the **Bharatiya Antariksh Hackathon 2026** for **Problem Statement 13 – Air-Gapped Predictive Copilot for Secure MPLS Operations**.
