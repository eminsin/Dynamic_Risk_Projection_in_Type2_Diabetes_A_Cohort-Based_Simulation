# Dependencies
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

# 1.  Screen HbA1c (H) per patient  ------------------------------------------
screen_H = (
    df.loc[df["Year"] == 1, ["Patient_ID", "HbA1c"]]
      .set_index("Patient_ID")["HbA1c"]
)

# 2.  Sort for cumulative calculations
df_sorted = df.sort_values(["Patient_ID", "Year"]).copy()

# 3.  Cumulative mean HbA1c (A) for each patient up to current year ----------
df_sorted["CumMean_HbA1c"] = (
    df_sorted.groupby("Patient_ID")["HbA1c"]
             .expanding()
             .mean()
             .reset_index(level=0, drop=True)
)

# 4.  Merge screen_H into df_sorted so every row has H ------------------------
df_sorted["Screen_HbA1c"] = df_sorted["Patient_ID"].map(screen_H)

# 5.  Hazard calculation parameters (DCCT Poisson model) ---------------------
ALPHA = -10.682
B1 = 0.201
B2 = 0.561
B3 = -1.228
B4 = 1.709
B5 = 0.686

# 6.  Compute hazard λ_it -----------------------------------------------------
#    D = Year, t = Diabetes_Duration, A = CumMean_HbA1c
ln_D = np.log(df_sorted["Year"])
ln_A = np.log(df_sorted["CumMean_HbA1c"])

df_sorted["Hazard"] = np.exp(
    ALPHA +
    B1 * df_sorted["Screen_HbA1c"] +
    B2 * ln_D +
    B3 * df_sorted["Diabetes_Duration"] +
    B4 * ln_A +
    B5 * df_sorted["Diabetes_Duration"] * ln_A
)

# 7.  Collect output DataFrame -----------------------------------
hazard_df = df_sorted[[
    "Bootstrap", "Year", "Diabetes_Duration", "Patient_ID",
    "Sex", "Ethnicity", "CumMean_HbA1c", "Hazard"
]].reset_index(drop=True)

# hazard_df.to_csv("hazard_df.csv", index=False)

# Compute average hazard rate per study year (diabetes duration)
avg_hazard_diabetes_duration = (
    hazard_df.groupby("Diabetes_Duration", as_index=False)["Hazard"]
             .mean()
             .rename(columns={"Hazard": "Mean_Hazard"})
)
print(avg_hazard_diabetes_duration)

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_hazard_diabetes_duration, x='Diabetes_Duration', y='Mean_Hazard', marker='o', color='b')
plt.xlabel('Diabetes Duration')
plt.ylabel('Mean Hazard Estimate')
plt.title('Individual-level Mean Hazard Estimates')
plt.grid(False)
plt.show()

