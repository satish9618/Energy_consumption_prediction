import streamlit as st
import numpy as np
import joblib


model = joblib.load("model.pkl")  

st.title("🏠 Energy Consumption Predictor")
st.write("Enter building details below to predict energy usage (kWh).")


square_footage = st.number_input("Square Footage")
num_occupants = st.number_input("Number of Occupants", min_value=1, max_value=100, step=1)
appliances_used = st.number_input("Appliances Used", min_value=1, max_value=50, step=1)
avg_temp = st.number_input("Average Temperature (°C)", min_value=-20.0, max_value=50.0)


if st.button("Predict Energy Consumption"):
    input_data = np.array([[square_footage, num_occupants, appliances_used, avg_temp]])
    prediction = model.predict(input_data)[0]

    st.success(f"🔋 Predicted Energy Consumption: {prediction:.2f} kWh")
