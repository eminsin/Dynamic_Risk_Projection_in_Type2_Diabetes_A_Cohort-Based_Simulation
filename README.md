---

<p align="center">
  <img width="600" height="500" alt="image_summary of the project" src="https://github.com/user-attachments/assets/b9800488-0821-4f45-a351-82e6819c96cc" />
</p>

<h1 align="center">Dynamic Risk Projection in Type 2 Diabetes A Cohort-Based Simulation</h1>



---

## 🎯 Project Overview

This project provides a **_comprehensive simulation framework_** for modeling the progression of Type 2 Diabetes (T2D) over HbA1c level and evaluating diet, insulin and other therapies' **_treatment outcomes_** at **_both individual and population levels._** Using **_Dynamic Linear Models (DLMs)_** with patient-specific random effects, the framework generates a realistic longitudinal trajectory for a key risk factor, HbA1c.

Beyond **_risk-factor simulation,_** the project quantifies **_cumulative glycemic exposure,_** estimates **_diabetes-related complication hazards,_** derives **_annual event probabilities,_** and evaluates **_treatment efficiency over time._** These components enable the assessment of **_disease progression, long-term health outcomes, and intervention effectiveness_** within a unified modeling framework.

The simulated data can also be used to support the development of data-driven decision models, including Markov Decision Processes (MDPs), for optimizing treatment strategies and intervention timing.



---

## 🔬 Laboratory

+ Developed a **_comprehensive longitudinal simulation framework_** for Type 2 Diabetes progression using **_Dynamic Linear Models (DLMs), state-space modeling concepts, patient-specific random effects, and Monte Carlo simulation_** to generate realistic trajectories of a key clinical biomarker HbA1c while capturing patient heterogeneity and temporal disease dynamics.
+ Applied **_multivariate simulation, random-effects estimation, variance decomposition, distribution fitting, parameter calibration from published studies, uncertainty quantification_** and **_numerical integration techniques_** to quantify disease burden and risk and translate biomarker trajectories into clinically meaningful outcome predictions.
+ **_Designed and analyzed synthetic patient populations at both individual and cohort level_** to evaluate disease progression patterns, complication incidence, and treatment effectiveness across heterogeneous patient groups.
+ Integrated **_predictive analytics and real-world evidence methodologies_** by combining **_longitudinal data analysis, survival and risk modeling concepts, treatment response evaluation, and evidence synthesis_** from epidemiological studies to assess intervention outcomes and support **_future HEOR and disease-modeling applications._**

---



## 📂 Folder Structure

```
Dynamic_Risk_Projection_in_Type2_Diabetes_A_Cohort-Based_Simulation/
├── notebooks/
│   └── Simulation_HbA1c_All.ipynb                                           # Main walkthrough notebook  
├── data/
│   └──                                                                      # Simulated datasets
├── scripts/
│   └── 1- simulation_framework.py                                           # Step-by-step simulation and outcomes analysis
│   └── 2- data_visualization.py
│   └── 3- individual_level_hazard_rate.py
│   └── 4- individual_level_probability_of_having_a_chronic_disease.py
│   └── 5- individual_level_therapy_efficiency.py
│   └── 6- population_level_aggregation.py
├── images/
│   └── simulation_and_study_design.png                                      # Simulation design
├── README.md                                                                # Project overview (you are here)
└── LICENSE                                                                  # MIT License
```

---



## 🧠 Notebook Topics for Each Intervention: Other Therapies, Diet and Insulin

### 🧮 1. Longitudinal Data Simulation
+ 

### 🧮 2. HbA1c Trajectory Visualization
+ 

### 🧮 3. Individual-level Hazard
+ 

### 🧮 4. Individual-level Probability of Having a Chronic Disease
+ 

### 🧮 5. Individual-level Therapy/Intervention Efficiency
+ 

### 🧮 6. Population-level Aggregation (Hazard/Probability/Efficiency)
+ 

### 🧮 7. Sensitivity Analysis (for Other Therapies only)
+ 


---



## 🛠 Built With

- Python 3.12
- `numpy`, `pandas`, `seaborn`, `matplotlib` 
- Jupyter Notebook

---



## 🌱 Inspired By
- ** by  et al.

---



## 🤝 Connect

Feel free to reach out or star this repo!

Let’s learn together. 🌱
