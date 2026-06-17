---

<p align="center">
  <img width="600" height="500" alt="image_summary of the project" src="https://github.com/user-attachments/assets/b9800488-0821-4f45-a351-82e6819c96cc" />
</p>

<h1 align="center">Dynamic Risk Projection in Type 2 Diabetes A Cohort-Based Simulation</h1>



---

## 🎯 Project Overview

This project provides a **_comprehensive simulation framework_** for modeling the progression of Type 2 Diabetes (T2D) over HbA1c level and evaluating diet, insulin and other therapies' **_treatment outcomes_** at **_both individual and population levels._** Using **_Dynamic Linear Models (DLMs)_** with patient-specific random effects, the framework generates a realistic longitudinal trajectory for a key risk factor, HbA1c.

Beyond **_risk-factor simulation,_** the project quantifies **_cumulative glycemic exposure,_** estimates **_diabetes-related complication hazards,_** derives **_annual event probabilities,_** and evaluates **_treatment effectiveness over time._** These components enable the assessment of **_disease progression, long-term health outcomes, and intervention effectiveness_** within a unified modeling framework.

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
│   └── Simulation_HbA1c_All.ipynb                                          # Main walkthrough notebook  
├── data/
│   └── simulated_data_other_therapies.csv                                  # Dataset simulated to get HbA1c tracejtory for other therapies
│   └── hazard_df_other_therapies.csv                                       # Hazard rates
│   └── probability_df_other_therapies.csv                                  # Probabilities of having a chronic disease 
│   └── beta_df_other_therapies.csv                                         # Other therapies' effectiveness for the metric beta produced
│   └── population_hazard_probability_beta_df_other_therapies.csv           # Population-level aggregation for other therapies
│   └── simulated_data_diet.csv                                             # Dataset simulated to get HbA1c tracejtory for diet
│   └── hazard_df_diet.csv                                                  # Hazard rates
│   └── probability_df_diet.csv                                             # Probabilities of having a chronic disease
│   └── beta_df_other_diet.csv                                              # Diet's effectiveness for the metric beta produced
│   └── population_hazard_probability_beta_df_diet.csv                      # Population-level aggregation for diet
│   └── simulated_data_insulin.csv                                          # Dataset simulated to get HbA1c tracejtory for insulin
│   └── hazard_df_insulin.csv                                               # Hazard rates
│   └── probability_df_insulin.csv                                          # Probabilities of having a chronic disease
│   └── beta_df_insulin.csv                                                 # Insulin's effectiveness for the metric beta produced
│   └── population_hazard_probability_beta_df_insulin.csv                   # Population-level aggregation for diet                                  
├── scripts/
│   └── 1- simulation_framework.py                                          # Step-by-step simulation and outcomes analysis for each therapy method
│   └── 2- data_visualization.py
│   └── 3- individual_level_hazard_rate.py
│   └── 4- individual_level_probability_of_having_a_chronic_disease.py
│   └── 5- individual_level_therapy_effectiveness.py
│   └── 6- population_level_aggregation.py
├── images/
│   └── simulation_and_study_design.png                                      # Simulation design
├── README.md                                                                # Project overview (you are here)
└── LICENSE                                                                  # MIT License
```

---



## 🧠 Notebook Topics for Each Intervention: Other Therapies, Diet and Insulin

### 🧮 1. Longitudinal Data Simulation
+ Simulated the longitudinal trajectory of HbA1c using Dynamic Linear Models with patient-specific random effects to capture both disease progression and inter-patient variability.
+ Generated synthetic patient cohorts based on literature-derived parameters, enabling the study of long-term disease dynamics when real-world patient-level data are unavailable.
+ Incorporated therapy-specific treatment effects into biomarker evolution, allowing direct comparison of intervention scenarios under a common modeling framework.
+ Produced realistic patient-level datasets that serve as the foundation for all subsequent risk, probability, and effectiveness analyses.

### 🧮 2. HbA1c Trajectory Visualization
+ Visualized individual and population-level biomarker trajectories to identify trends, variability, and treatment response heterogeneity.
+ Compared simulated trajectories against expected clinical behavior reported in the literature to assess model plausibility.
+ Generated interpretable visual summaries that support understanding of disease progression and intervention impact over time.

### 🧮 3. Individual-level Hazard
+ Estimated patient-specific complication hazards using longitudinal HbA1c trajectories and published risk relationships from epidemiological studies.
+ Modeled how changing glycemic exposure influences future complication risk throughout the simulation horizon.
+ Quantified the dynamic risk profile of each patient by continuously updating hazard estimates as biomarker values evolved.
+ Produced individualized risk trajectories that allow comparison of long-term clinical outcomes across therapies.

### 🧮 4. Individual-level Probability of Having a Chronic Disease
+ Translated estimated hazard rates into annual probabilities of developing diabetes-related chronic complications.
+ Examined how patient characteristics, disease progression, and treatment response affect future disease risk.
+ Evaluated risk accumulation over time, providing an intuitive interpretation of complication likelihood at the individual level.
+ Generated clinically interpretable probability estimates suitable for outcome assessment and treatment comparison.

### 🧮 5. Individual-level Therapy/Intervention Effectiveness
+ Assessed treatment effectiveness by measuring changes in glycemic burden, complication hazards, and disease probabilities relative to previous year's conditions.
+ Quantified therapy performance for each simulated patient, including variability in treatment response across heterogeneous populations.
+ Produced patient-level effectiveness metric (Beta) that can support personalized treatment evaluation and comparative effectiveness research.

### 🧮 6. Population-level Aggregation (Hazard/Probability/Efficiency)
+ Aggregated individual simulation results to estimate population-level treatment outcomes and disease burden.
+ Calculated cohort-average hazards, complication probabilities, and treatment efficiency measures for each intervention strategy.
+ Generated population-level evidence that supports comparative assessment of therapies and broader health outcomes research applications.

### 🧮 7. Sensitivity Analysis (for Other Therapies only)
+ Investigated the robustness of model outcomes under varying treatment assumptions and therapy-specific parameter settings.
+ Evaluated how uncertainty in intervention effects propagates through biomarker trajectories, hazards, probabilities, and efficiency metrics.
+ Compared alternative therapeutic scenarios to identify parameters with the greatest influence on long-term outcomes.
+ Demonstrated the stability and reliability of the simulation framework while highlighting key drivers of treatment effectiveness.



---



## 🛠 Built With

- Python 3.12
- `numpy`, `pandas`, `seaborn`, `matplotlib` 
- Jupyter Notebook

---



## 🌱 Inspired By
- *Estimating risk factor progression equations for the UKPDS Outcomes Model 2 (UKPDS 90)* by Leal et al.
- *The Relationship of Glycemic Exposure (HbA1c) to the Risk of Development and Progression of Retinopathy in the Diabetes Control and Complications Trial* by The Diabetes Control and Complications Trial Research Group
- *Estimates of Absolute Cause-Specific Risk in Cohort Studies* by J. Benichou and Mitchell H. Gail
- *Effect of Patients’ Risks and Preferences on Health Gains With Plasma Glucose Level Lowering in Type 2 Diabetes Mellitus* by Vijan et al.



---



## 🤝 Connect

Feel free to reach out or star this repo!

Let’s learn together. 🌱
