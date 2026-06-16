import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# Assumes `df` already exists in the notebook from the user's HbA1c simulation
# ---------------------------------------------------------------------------
try:
    df
except NameError:
    raise RuntimeError(
        "The DataFrame `df` was not found. "
        "Please run your HbA1c simulation code first, "
        "so that `df` containing the columns "
        "['Bootstrap', 'Year', 'Diabetes_Duration', 'Patient_ID', "
        "'Sex', 'Ethnicity', 'HbA1c'] is defined."
    )

# Compute average HbA1c level per study year (diabetes duration)
avg_HbA1c_diabetes_duration = (
    df.groupby("Diabetes_Duration", as_index=False)["HbA1c"]
             .mean()
             .rename(columns={"HbA1c": "Mean_HbA1c"})
)
print(avg_HbA1c_diabetes_duration)

avg_df = avg_HbA1c_diabetes_duration.copy()

# harmonise column names
if "Avg_HbA1c" not in avg_df.columns:
    # try to detect the HbA1c column
    hba1c_col = [c for c in avg_df.columns if "HbA1c" in c][0]
    avg_df = avg_df.rename(columns={hba1c_col: "Avg_HbA1c"})

# Ensure Diabetes_Duration integer & sorted
avg_df["Diabetes_Duration"] = avg_df["Diabetes_Duration"].astype(int)
avg_df = avg_df.sort_values("Diabetes_Duration").reset_index(drop=True)

# ---------------------------------------------------------------------------
# 1. cumulative mean HbA1c (A) across durations for the population
avg_df["CumMean_HbA1c"] = avg_df["Avg_HbA1c"].expanding().mean()

# 2. baseline H (duration 0 average)
baseline_H = float(avg_df.loc[avg_df["Diabetes_Duration"] == 0, "Avg_HbA1c"].iloc[0])

# 3. Hazard calculation parameters
ALPHA = -10.682
B1 = 0.201
B2 = 0.561
B3 = -1.228
B4 = 1.709
B5 = 0.686

# 4. Calculate hazard for each duration
#    D = Year = duration + 1
avg_df["Year"] = avg_df["Diabetes_Duration"] + 1
avg_df["ln_D"] = np.log(avg_df["Year"])
avg_df["ln_A"] = np.log(avg_df["CumMean_HbA1c"])

avg_df["Hazard"] = np.exp(
    ALPHA +
    B1 * baseline_H +
    B2 * avg_df["ln_D"] +
    B3 * avg_df["Diabetes_Duration"] +
    B4 * avg_df["ln_A"] +
    B5 * avg_df["Diabetes_Duration"] * avg_df["ln_A"]
)

# 5. Beta calculation (skip first duration)
haz_prev = avg_df["Hazard"].shift(1)
Hb_prev  = avg_df["Avg_HbA1c"].shift(1)

beta_vals = np.where(
    (avg_df["Diabetes_Duration"] == 0) | (haz_prev <= 0) | (avg_df["Hazard"] <= 0) |
    (avg_df["Avg_HbA1c"] == Hb_prev),
    np.nan,
    np.log(avg_df["Hazard"] / haz_prev) / np.log(avg_df["Avg_HbA1c"] / Hb_prev)
)

avg_df["Beta"] = beta_vals

# Keep desired columns
pop_hazard_beta_df = avg_df[[
    "Diabetes_Duration", "Year", "Avg_HbA1c", "CumMean_HbA1c",
    "Hazard", "Beta"
]]

avg_df["Probability"] = 1.0 - np.exp(
    - pop_hazard_beta_df["Hazard"] * pop_hazard_beta_df["Year"]
)

pop_hazard_beta_df = avg_df[[
    "Diabetes_Duration", "Year", "Avg_HbA1c", "CumMean_HbA1c",
    "Hazard", "Probability", "Beta"
]]

print(pop_hazard_beta_df)

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=pop_hazard_beta_df, x='Diabetes_Duration', y='Hazard', marker='o', color='b')
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean Hazard Estimate')
plt.title('Population-level Mean Hazard Estimate')
plt.grid(False)
plt.show()

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=pop_hazard_beta_df, x='Diabetes_Duration', y='Probability', marker='o', color='b')
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean Probability Estimate')
plt.title('Population-level Mean Probability Estimates')
plt.grid(False)
plt.show()

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=pop_hazard_beta_df, x='Diabetes_Duration', y='Beta', marker='o', color='b')
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean Beta Estimate')
plt.title('Population-level Average Therapy Efficiency Estimates')
plt.grid(False)
plt.show()

