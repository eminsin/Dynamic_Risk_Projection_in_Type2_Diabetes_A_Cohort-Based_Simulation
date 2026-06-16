# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mapping for Sex and Ethnicity
sex_map = {0: 'Male', 1: 'Female'}
ethnicity_map = {0: 'White & Other', 1: 'Asian-Indian', 2: 'Afro-Caribbean'}

custom_palette = {
    0: '#9467bd',   # purple → White & Other
    1: '#ffbf00',   # yellow → Asian-Indian
    2: '#2ca02c'    # green  → Afro-Caribbean
}

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Diabetes_Duration', y='HbA1c', errorbar=('ci', 95), estimator='mean')
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean HbA1c Level')
plt.title('Simulated Progression of HbA1c Levels for Other Therapies')
plt.grid(False)
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Diabetes_Duration', y='HbA1c', hue='Sex', errorbar=None, estimator='mean', palette='coolwarm')
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean HbA1c Level')
plt.title('HbA1c Levels for Other Therapies by Sex')
plt.grid(False)
plt.legend(title='Sex', labels=sex_map.values())
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Diabetes_Duration', y='HbA1c', hue='Ethnicity', errorbar=None, estimator='mean', 
             palette=custom_palette, hue_order=[0, 1, 2])
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean HbA1c Level')
plt.title('HbA1c Levels for Other Therapies by Ethnicity')
plt.grid(False)
plt.legend(
    title='Ethnicity',
    labels=[ethnicity_map[i] for i in [0, 1, 2]])
plt.show()

