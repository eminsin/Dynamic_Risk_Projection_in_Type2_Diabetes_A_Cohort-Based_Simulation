import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# Assumes `hazard_df` already exists in the notebook from the user's HbA1c simulation
# ---------------------------------------------------------------------------
try:
    hazard_df
except NameError:
    raise RuntimeError(
        "The DataFrame `hazard_df` was not found. "
        "Please run your HbA1c simulation and individual level hazard rate codes first, "
        "so that `hazard_df` containing the columns "
        "['Bootstrap', 'Year', 'Diabetes_Duration', 'Patient_ID', "
        "'Sex', 'Ethnicity', 'CumMean_HbA1c', 'Hazard'] is defined."
    )

# 1. Copy relevant columns so we keep the original frame intact
probability_df = hazard_df.copy()

# 2. Probability of disease event in year t for each patient
#    P = 1 - exp(-rate * time),  where time = Year (1…21) and rate = Hazard
probability_df["Probability"] = 1.0 - np.exp(
    - probability_df["Hazard"] * probability_df["Year"]
)

# 3. Keep only necessary columns (add others if you need them)
probability_df = probability_df[[
    "Bootstrap", "Year", "Diabetes_Duration", "Patient_ID", "Probability"
]]

# probability_df.to_csv("probability_df.csv", index=False)

# Compute average probability per study year (diabetes duration)
avg_probability_diabetes_duration = (
    probability_df.groupby("Diabetes_Duration", as_index=False)["Probability"]
             .mean()
             .rename(columns={"Probability": "Mean_Probability"})
)
print(avg_probability_diabetes_duration)

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_probability_diabetes_duration, x='Diabetes_Duration', y='Mean_Probability', marker='o', color='b')
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean Probability Estimate')
plt.title('Individual-level Mean Probability Estimates')
plt.grid(False)
plt.show()
