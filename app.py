
import streamlit as st
import joblib

model = joblib.load("income_model.pkl")

st.title("Income Prediction App")

age = st.slider("Age", 18, 70, 30)
education = st.slider("Education Level (0 = Least, 15 = Most)", 0, 15, 10)
gender = st.selectbox("Gender", ["Male", "Female"])
hours = st.slider("Hours Per Week", 1, 100, 40)

gender_encoded = 1 if gender == "Male" else 0

if st.button("Predict Income Category"):
    prediction = model.predict([[age, education, gender_encoded, hours]])
    label = ">50K" if prediction[0] == 1 else "<=50K"
    st.success(f"Predicted Income: {label}")
