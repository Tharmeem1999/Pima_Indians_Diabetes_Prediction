# Pima Indians Diabetes Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)

## Project Overview
This project is a Machine Learning application designed to predict whether a female patient has diabetes based on diagnostic measurements. The model is trained on the **Pima Indians Diabetes Database** and deployed using a **Streamlit** web application for interactive use.

The project focuses heavily on **Data Quality**, implementing advanced imputation techniques for missing values (e.g., Insulin, SkinThickness) and careful outlier handling to ensure robust predictions.

## 📂 Repository Structure
```text
├── diabetes.csv                       # The original dataset
├── Pima_Diabetes.ipynb                # Jupyter Notebook (EDA, Preprocessing, Model Training)
├── diabetes_app.py                    # Streamlit Web Application
├── Pima_Indians_Diabetes_model.pickle # Trained Machine Learning Model
└── README.md                          # Project Documentation

```

## Dataset Description
The dataset comes from the kaggle. [Link](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

Rows: 768

Columns: 9

Target: Outcome (0 = Non-Diabetic, 1 = Diabetic)

| Feature                   | Description                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------|
| Pregnancies               | Number of times pregnant                                                                   |
| Glucose                   | Plasma glucose concentration 2 hours into an oral glucose tolerance test                  |
| BloodPressure             | Diastolic blood pressure (mm Hg)                                                           |
| SkinThickness             | Triceps skin fold thickness (mm)                                                           |
| Insulin                   | 2-hour serum insulin (mu U/ml)                                                             |
| BMI                       | Body mass index (weight in kg/(height in m)^2)                                            |
| DiabetesPedigreeFunction  | Function scoring likelihood of diabetes based on family history                           |
| Age                       | Age (years)                                                                               |

## Methodology
1. **Data Cleaning & Preprocessing**
   
A major challenge with this dataset is the presence of invalid "0" values in biological columns (Glucose, Blood Pressure, Skin Thickness, Insulin, BMI).

    * **Problem**: Biological stats cannot be zero. These represented missing data.

    * **Solution** (Group-Aware Imputation): Instead of using a global mean/median, missing values were filled using the median of the specific Outcome group.

        * **Example**: Missing Insulin for a diabetic patient was filled with the median Insulin of other diabetic patients (~169.5), rather than the healthy median (~102.5).

2. **Outlier Removal**
   
Statistical outliers were handled using the IQR (Interquartile Range) Method and domain knowledge:

    * **SkinThickness**: Removed records < 14.5 (for Diabetics) and > 42.5 (for Non-Diabetics) to reduce noise.
    
    * **Extreme Values**: Removed physically impossible outliers (e.g., SkinThickness = 99).
    
    * **Pregnancies**: High pregnancy counts (e.g., 14-17) were kept as they were found to be valid high-risk indicators for diabetes in this specific dataset.
