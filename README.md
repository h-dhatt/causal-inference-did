# Causal Inference with Difference-in-Differences

This project uses **causal inference techniques** to estimate treatment effects from observational data, focusing on the Difference-in-Differences (DiD) framework. Applications include evaluating policy changes, interventions, and natural experiments.

## Methods
- Implemented Difference-in-Differences with:
  - Two-way fixed effects models
  - Pre-trend checks
- Conducted robustness analyses with alternative specifications
- Visualized treatment and control group dynamics over time

## Results
- DiD successfully identified treatment effects in simulated and real-world datasets.
- Placebo tests confirmed validity of causal assumptions.
- Results highlight the importance of parallel trends and robustness checks.

## Repository Structure
- `notebooks/`: Jupyter notebooks with DiD applications
- `src/`: Functions for treatment effect estimation
- `results/`: Event-study plots, regression outputs
- `README.md`: Project documentation

## Keywords
Causal Inference, Econometrics, Difference-in-Differences, Treatment Effects, Policy Evaluation
