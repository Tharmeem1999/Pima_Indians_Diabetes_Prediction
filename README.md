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

Feature	Description
Pregnancies	Number of times pregnant
Glucose	Plasma glucose concentration a 2 hours in an oral glucose tolerance test
BloodPressure	Diastolic blood pressure (mm Hg)
SkinThickness	Triceps skin fold thickness (mm)
Insulin	2-Hour serum insulin (mu U/ml)
BMI	Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction	A function scoring likelihood of diabetes based on family history
Age	Age (years)
