import streamlit as st
import requests

API_URL = "https://stroke-prediction-api-aksd.onrender.com/predict"

st.set_page_config(page_title="Stroke Risk Predictor", page_icon="🩺", layout="centered")
st.title("Stroke Risk Prediction System")
st.write("Enter your health details below. The system will predict your stroke risk using a machine learning model.")

with st.form("input_form"):
    age = st.number_input("Age", 1, 120)
    gender = st.selectbox("Gender", ["Male", "Female"])
    heart_disease = st.selectbox("Heart Disease?", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    marital_status = st.selectbox("Marital Status", ["Single", "Married"])
    work_type = st.selectbox("Work Type", ["Private","Self-employed","Govt","Children","Never-worked"])
    residence_type = st.selectbox("Residence Type", ["Rural", "Urban"])
    avg_glucose_level = st.number_input("Average Glucose Level", 50.0, 300.0)
    bmi = st.number_input("Body Mass Index (BMI)", 10.0, 60.0)
    smoking_status = st.selectbox("Smoking Status", ["never smoked", "formerly smoked", "smokes"])
    alcohol_intake = st.selectbox("Alcohol Intake", ["No", "Yes"])
    physical_activity = st.selectbox("Physical Activity", ["No", "Yes"])
    stroke_history = st.selectbox("Stroke History", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    family_history_stroke = st.selectbox("Family History of Stroke", ["No", "Yes"])
    dietary_habits = st.selectbox("Dietary Habits", ["No", "Yes"])
    stress_levels = st.number_input("Stress Levels (0-10)", 0.0, 10.0, step=0.1)
    symptoms = st.selectbox("Symptoms Present?", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    systolic_bp = st.number_input("Systolic BP", 80, 200)
    diastolic_bp = st.number_input("Diastolic BP", 50, 130)
    hdl = st.number_input("HDL", 20, 100)
    ldl = st.number_input("LDL", 20, 200)
    submitted = st.form_submit_button("Predict Stroke Risk")

if submitted:
    stroke_score = (
        age*0.3 +
        avg_glucose_level*0.4 +
        bmi*0.2  # example weighting
    )

    data = {
        "age": int(age),
        "gender": gender,
        "heart_disease": int(heart_disease),
        "marital_status": marital_status,
        "work_type": work_type,
        "residence_type": residence_type,
        "avg_glucose_level": float(avg_glucose_level),
        "bmi": float(bmi),
        "smoking_status": smoking_status,
        "alcohol_intake": alcohol_intake,
        "physical_activity": physical_activity,
        "stroke_history": int(stroke_history),
        "family_history_stroke": family_history_stroke,
        "dietary_habits": dietary_habits,
        "stress_levels": float(stress_levels),
        "symptoms": int(symptoms),
        "systolic_bp": int(systolic_bp),
        "diastolic_bp": int(diastolic_bp),
        "hdl": int(hdl),
        "ldl": int(ldl),
        "stroke_score": float(stroke_score)  # include this
    }


    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            probability = result["probability"]

            if prediction == 1:
                st.error(f"⚠️ High Stroke Risk (Probability: {probability:.2f})")
            else:
                st.success(f"🟢 Low Stroke Risk (Probability: {probability:.2f})")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error: {e}")


