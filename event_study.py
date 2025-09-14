import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root/'data'/'panel.csv')

# compute relative time to treatment (= year - adoption year). We need adoption year per unit.
adopt_year = df[df['treat']==1].groupby('unit')['year'].min().rename('adopt_year')
df = df.merge(adopt_year, on='unit', how='left')
df['rel_time'] = df['year'] - df['adopt_year']
# aggregate event study means
evt = df.groupby('rel_time')['y'].mean().reset_index()
plt.figure()
plt.plot(evt['rel_time'], evt['y'])
plt.axvline(0, linestyle='--')
plt.title('Event Study: Mean Outcome Around Adoption')
plt.xlabel('Years Relative to Adoption'); plt.ylabel('Mean y')
(root/'outputs').mkdir(exist_ok=True)
plt.tight_layout()
plt.savefig(root/'outputs'/'event_study.png', dpi=150)
print('Saved event study plot.')