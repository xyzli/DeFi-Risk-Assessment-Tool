# DeFi-Risk-Assessment-Tool

## Overview
This (very rudimentary) project predicts the volatility of Ethereum prices using historical market data. It includes a Streamlit dashboard for interactive predictions and visualizations. I plan to include a smart contract risk model as a feature in the future.

I used random forest regressor to leverage multiple decision trees to capture the non-linear market data. This reduces the risk of overfitting and handles missing or outlier datapoints. With a larger dataset, I would consider a neural network instead.

## Project Structure
project/

├── data/ # Ethereum Market Data

│ └──  ETH_data.csv

├── models/ # Trained model

│ └── market_volatility_model.pkl

├── dashboard.py # Streamlit dashboard

├── requirements.txt # Dependencies to download

└── README.md

## Installation
1. Clone this repository:
   git clone https://github.com/xyzli/DeFi-Risk-Assessment-Tool.git
   
2. Install dependencies while inside the project directory.
   pip install -r requirements.tx
   
3. Run Streamlit dashboard
   streamlit run dashboard.py
