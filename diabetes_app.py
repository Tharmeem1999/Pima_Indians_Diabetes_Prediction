import streamlit as st
import pickle
import numpy as np

# Load the saved model
def load_model():
    with open("Pima_Indians_Diabetes_model.pickle", "rb") as f:
        model = pickle.load(f)
    return model

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model File 'Pima_Indians_Diabetes_model.pickle' not found. Please run your notebook to generate it.")
    st.stop()

# --- WEB INTERFACE CODE --- 

# Title
st.title("Pima Diabetes Prediction Interface")
st.write("Enter the female patient details below to estimate the risk.") 

# Using a form to keep structure vertical and clean
with st.form("diabetes_form"):

    # 1. Pregnancies
    pregnancies = st.text_input("Pregnancies", value="0")

    # 2. Glusoce
    glucose = st.text_input("Glucose level (mg/dL)", value="100")

    # 3. Blood Pressure
    bp = st.text_input("Blood Pressure level (mm Hg)", value="70")

    # 4. Skin Thickness
    skin = st.text_input("Skin Thickness (mm)", value="20")
    
    # 5. Insulin
    insulin = st.text_input("Insulin level (mu U/ml)", value="79")

    # 6. BMI (Added this as your model requires it)
    bmi = st.text_input("BMI (Body Mass Index)", value="30.0")
    
    # 7. Diabetes Pedigree Function
    dpf = st.text_input("Diabetes Pedigree Function", value="0.5")
    
    # 8. Age
    age = st.text_input("Age (years)", value="30")

    # Submit Button
    submit_button = st.form_submit_button("Predict")

# Logic to run when button is clicked
if submit_button:
    try:
        # Convert inputs to float (text inputs return strings)
        features = np.array([[
            float(pregnancies),
            float(glucose),
            float(bp),
            float(skin),
            float(insulin),
            float(bmi),
            float(dpf),
            float(age)
        ]])

        # Make prediction
        prediction = model.predict(features)

        # Display Result
        st.subheader("Prediction Result:")
        if prediction[0] == 1:
            st.error("The model predicts: Positive for Diabetes")
        else:
            st.success("The model predicts: Negative for Diabetes")
            
    except ValueError:
        st.warning("Please enter valid numeric values for all fields.")