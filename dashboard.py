import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

#DeFi Risk Assessment Tool
#My first dashboard!
#Nathan Li

DATA_PATH = os.path.join("data", "ETH_data.csv")
MODEL_PATH = os.path.join("models", "ETH_model.pkl")

model = joblib.load(MODEL_PATH) #trained model

#Sidebar stuff
st.title("DeFi Market Volatility Predictor")
st.sidebar.header("Input Features")

price = st.sidebar.number_input("Price", value=3000.0)
returns = st.sidebar.number_input("Returns (%)", value=0.02)
moving_avg_10 = st.sidebar.number_input("10-Day Moving Avg", value=2900.0)
moving_avg_50 = st.sidebar.number_input("50-Day Moving Avg", value=2800.0)

input_data = pd.DataFrame({
    "price": [price],
    "returns": [returns],
    "moving_avg_10": [moving_avg_10],
    "moving_avg_50": [moving_avg_50]
})

st.subheader("User Inputs") #inputs
st.write(input_data)

if st.sidebar.button("Predict Volatility"):
    prediction = model.predict(input_data)
    st.subheader("Prediction")
    st.success(f"Predicted Volatility: {prediction[0]:.6f}")

#Dashboard labels
st.subheader("Historical Volatility Trends")
data = pd.read_csv(DATA_PATH)
fig, ax = plt.subplots()
ax.plot(data["timestamp"], data["volatility"], label="Volatility")
ax.set_xlabel("Timestamp (Every 30 Days)")
ax.xaxis.set_major_locator(mdates.DayLocator(interval=30))
ax.set_ylabel("Volatility")
plt.xticks(rotation=45)
st.pyplot(fig)