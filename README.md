# Project 7 — Causal Inference: Difference-in-Differences (Synthetic Panel)

**Goal:** Estimate an average treatment effect using DiD on a simulated policy adoption.

## Highlights
- Simulated staggered adoption data with unit and time fixed effects
- Plain OLS with dummies (no external libs) to demonstrate identification
- Robustness: event-study style leads/lags visualization

## Structure
```
Project7_Causal_Inference_DiD/
  ├─ data/
  │   └─ panel.csv
  ├─ outputs/
  ├─ src/
  │   ├─ simulate.py
  │   ├─ did_simple.py
  │   └─ event_study.py
  ├─ requirements.txt
  └─ README.md
```

## Quickstart
```bash
pip install -r requirements.txt
python src/simulate.py
python src/did_simple.py
python src/event_study.py
```
