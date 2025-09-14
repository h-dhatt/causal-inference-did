import pandas as pd, numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root / 'data' / 'panel.csv')
# two-way FE via dummy OLS: y ~ treat + unit dummies + year dummies
y = df['y'].values
unit_d = pd.get_dummies(df['unit'].astype(int), prefix='u', drop_first=True)
year_d = pd.get_dummies(df['year'].astype(int), prefix='t', drop_first=True)
X = pd.concat([df[['treat']], unit_d, year_d], axis=1).values

lr = LinearRegression(fit_intercept=True)
lr.fit(X, y)
coef_treat = lr.coef_[0]
print(f"DiD estimate (treat coef) ~ {coef_treat:.3f}")

with open(root/'outputs'/'did_estimate.txt','w') as f:
    f.write(f'DiD treat coefficient: {coef_treat:.3f}\n')

# plot means by year
mean_by_year = df.groupby('year')['y'].mean()
plt.figure()
mean_by_year.plot()
plt.title('Outcome Means by Year')
plt.tight_layout()
(root/'outputs').mkdir(exist_ok=True)
plt.savefig(root/'outputs'/'means_by_year.png', dpi=150)