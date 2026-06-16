# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set simulation parameters (for other therapies)
num_patients = 4675
num_years = 21
num_bootstraps = 1

"""
For a block lasting L years with target cumulative loss R (e.g. R = 0.12 for 12 %),

p = 1 - [(1 - R) ** 1/L]

"""

# Annual dropout probabilities for each period (for other therapies)
dropout_rates = { 
    1:  0.0210802, 2:  0.0210802, 3:  0.0210802, 4:  0.0210802,  5:  0.0210802, 6:  0.0210802,
    7:  0.0342697, 8:  0.0342697, 9:  0.0342697, 10: 0.0342697, 11:  0.0342697,
    12: 0.1259948, 13: 0.1259948, 14: 0.1259948, 15: 0.1259948, 16:  0.1259948,   
    17: 0.3211966, 18: 0.3211966, 19: 0.3211966, 20: 0.3211966, 21:  0.3211966
}

# Provided annual means and SDs in the 20-years span (for other therapies)
means = [6.5, 6.6, 6.8, 7.0, 7.3, 7.5, 7.7, 7.9, 8.0, 8.2,
         8.3, 8.3, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.3, 8.4]

sds = [1.4, 1.5, 1.6, 1.7, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8,
       1.8, 1.8, 1.8, 1.8, 1.7, 1.7, 1.7, 1.8, 1.8, 1.7, 1.8]

# Fixed Effect (coefficients)
# actual estimates (for other therapies)
phi_0 = 1.419
phi_1 = 0.724
gamma = 0.141
phi_2 = 0.081
phi_3 = 0.054
beta_ethnicity = [0.046, 0.066]

# Random Effect (epsilon + Mu)
# MU (unobserved time-invariant effect) has been omitted.
# EPSILON = N(0, sigma^2)

# (Calibrated) sigma (for other therapies)
sigma = 1.2

# Initialize Patient Data (for other therapies)
np.random.seed(42)
patient_ids = np.arange(num_patients)
sex = np.random.choice([0, 1], num_patients)                                  # 0=male, 1=female
ethnicity = np.random.choice([0, 1, 2], num_patients)                         # 0=reference, 1=Asian-Indian, 2=Afro-Caribbean
year_1 = np.random.normal(loc=means[0], scale=sds[0], size=num_patients)      # Initial HbA1c values


# Simulate and Store Data (for other therapies)

all_bootstrap_data = []

for b in range(num_bootstraps):
    data = []

    # Active patient list starts with everyone
    active_patients = set(patient_ids)

    # Store past values per patient
    patient_history = {pid: year_1[i] for i, pid in enumerate(patient_ids)}
    
    for t in range(1, num_years + 1):
        
        new_active_patients = set()                      # Keep track of patients who stay
        
        for i in list(active_patients):                  # Iterate over active patients only
            
            y_prev = patient_history[patient_ids[i]]     # Retrieve last year's value
            
            diabetes_duration = np.log(t) if t > 1 else 0
            
            # Assign ethnicity effect correctly
            ethnicity_effect = beta_ethnicity[ethnicity[i] - 1] if ethnicity[i] > 0 else 0
            
            # Compute new risk factor value
            y_new = (
                phi_0 + phi_1 * y_prev + gamma * diabetes_duration +
                phi_2 * year_1[i] + phi_3 * sex[i] + ethnicity_effect  
                + np.random.normal(0, sigma)  # Add noise
            )
            
            # Store results
            data.append({
                'Bootstrap': b + 1, 'Year': t, 'Diabetes_Duration': t-1, 'Patient_ID': patient_ids[i], 'Sex': sex[i],
                'Ethnicity': ethnicity[i], 'HbA1c': y_new
            })
            
            # Update patient's previous value for next iteration
            patient_history[patient_ids[i]] = y_new
                        
            # Apply dropout condition dynamically based on year
            if np.random.rand() > dropout_rates[t]:  # Keep patient if they don't drop out
                new_active_patients.add(i)
                        
        # Update active patients list for next year
        active_patients = new_active_patients
    
    all_bootstrap_data.extend(data)

# Covert to Dataframe
df = pd.DataFrame(all_bootstrap_data)
# df.to_csv("simulated_data.csv", index=False)
# print(df.head())
