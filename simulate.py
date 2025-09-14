import numpy as np, pandas as pd
from pathlib import Path

def simulate_panel(N=60, T=10, seed=0):
    rng = np.random.default_rng(seed)
    units = np.arange(N)
    years = np.arange(2010, 2010+T)
    adoptyear = rng.integers(2013, 2017, size=N)  # staggered
    rows = []
    true_tau = 2.0
    for i,u in enumerate(units):
        alpha_i = rng.normal(0,1)
        for t,year in enumerate(years):
            gamma_t = 0.2*(year-2010)  # time trend
            treat = 1 if year >= adoptyear[i] else 0
            eps = rng.normal(0,1)
            y = 5 + alpha_i + gamma_t + true_tau*treat + eps
            rows.append((u, year, treat, y))
    df = pd.DataFrame(rows, columns=['unit','year','treat','y'])
    return df

if __name__ == '__main__':
    df = simulate_panel()
    out = Path(__file__).resolve().parents[1] / 'data' / 'panel.csv'
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f'Wrote {out}, shape={df.shape}')