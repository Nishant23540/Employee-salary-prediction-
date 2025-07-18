import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("salary_model.pkl", "rb"))

# Set page title
st.set_page_config(page_title="Employee Salary Prediction", layout="centered")

st.title("💼 Employee Income Prediction")
st.write("Fill in the details below to predict whether an employee earns **>50K** or **<=50K** per year.")

# --- User Input Fields ---
age = st.number_input("Age", min_value=18, max_value=100, value=30)
education_num = st.slider("Education Level (numeric)", min_value=1, max_value=16, value=9)
hours_per_week = st.slider("Hours Worked Per Week", min_value=1, max_value=100, value=40)
capital_gain = st.number_input("Capital Gain", value=0)
capital_loss = st.number_input("Capital Loss", value=0)

gender = st.selectbox("Gender", ["Male", "Female"])
workclass = st.selectbox("Workclass", [
    "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov",
    "Local-gov", "State-gov", "Without-pay", "Never-worked"
])
occupation = st.selectbox("Occupation", [
    "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial",
    "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical",
    "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"
])

# --- Simple encoders (You should match these to your training encodings) ---
gender_map = {"Male": 1, "Female": 0}
workclass_map = {name: idx for idx, name in enumerate([
    "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov",
    "Local-gov", "State-gov", "Without-pay", "Never-worked"
])}
occupation_map = {name: idx for idx, name in enumerate([
    "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial",
    "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical",
    "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"
])}

# Encode selections
encoded_gender = gender_map[gender]
encoded_workclass = workclass_map.get(workclass, 0)
encoded_occupation = occupation_map.get(occupation, 0)

# --- Create input array ---
input_array = np.array([[age, encoded_workclass, 0, 0, education_num, 0, encoded_occupation, 0, 0,
                         encoded_gender, capital_gain, capital_loss, hours_per_week, 0]])

# --- Prediction ---
if st.button("🔍 Predict Income"):
    prediction = model.predict(input_array)[0]
    result = ">50K" if prediction == 1 else "<=50K"
    st.success(f"✅ Predicted Income: **{result}**")
