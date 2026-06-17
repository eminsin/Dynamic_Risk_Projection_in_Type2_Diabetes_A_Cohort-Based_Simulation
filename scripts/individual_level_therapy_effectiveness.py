import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# Assumes `df` and 'hazard_df' already exist in the notebook from the user's HbA1c simulation
# ---------------------------------------------------------------------------
try:
    df and hazard_df
except NameError:
    raise RuntimeError(
        "The DataFrame `df` and 'hazard_df' were not found. "
        "Please run your HbA1c simulation and individual-level hazard rate codes first, "
        "so that `merged` containing the columns "
        "['Bootstrap', 'Year', 'Diabetes_Duration', 'Patient_ID', "
        "'Sex', 'Ethnicity', 'CumMean_HbA1c', 'Hazard', 'HbA1c'] is defined."
    )

# 1. Merge hazard rates with corresponding HbA1c values -----------------------
merged = (
    hazard_df.merge(
        df[["Bootstrap", "Year", "Patient_ID", "HbA1c"]],
        on=["Bootstrap", "Year", "Patient_ID"],
        how="left",
        validate="one_to_one",
        suffixes=("", "_RiskFactor")
    )
)

# 2. Sort for lag calculations -------------------------------------------------
merged = merged.sort_values(["Patient_ID", "Year"]).copy()

# 3. Add previous-year values within each patient -----------------------------
merged["Hazard_prev"] = merged.groupby("Patient_ID")["Hazard"].shift(1)
merged["HbA1c_prev"]  = merged.groupby("Patient_ID")["HbA1c"].shift(1)

# 4. Calculate beta (skip Year==1 where prev is NaN) ---------------------------
def safe_beta(row):
    h_prev, h_cur = row["Hazard_prev"], row["Hazard"]
    a_prev, a_cur = row["HbA1c_prev"], row["HbA1c"]
    if pd.isna(h_prev) or pd.isna(a_prev):
        return np.nan
    if a_cur == a_prev or h_prev <= 0 or h_cur <= 0:
        return np.nan
    return np.log(h_cur / h_prev) / np.log(a_cur / a_prev)

merged["Beta"] = merged.apply(safe_beta, axis=1)

# 5. Prepare final beta DataFrame (exclude Year 1) -----------------------------
beta_df = merged.loc[merged["Year"] > 1, [
    "Bootstrap", "Year", "Diabetes_Duration", "Patient_ID", "Beta"
]].reset_index(drop=True)

#beta_df.to_csv("beta_df.csv", index=False)

# Compute average beta values per study year (diabetes duration)
avg_beta_diabetes_duration = (
    beta_df.groupby("Diabetes_Duration", as_index=False)["Beta"]
             .mean()
             .rename(columns={"Beta": "Mean_Beta"})
)
print(avg_beta_diabetes_duration)

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_beta_diabetes_duration, x='Diabetes_Duration', y='Mean_Beta', marker='o', color='b')
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean Beta Estimate')
plt.title('Individual-level Average Therapy Efficiency Estimates')
plt.grid(False)
plt.show()
