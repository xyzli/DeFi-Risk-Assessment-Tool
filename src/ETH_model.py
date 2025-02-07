import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import os

#Data stuff
PROJECT_PATH = os.path.dirname(os.getcwd())
DATA_PATH = os.path.join(PROJECT_PATH, "data", "ETH_data.csv")
MODEL_PATH = os.path.join(PROJECT_PATH, "models", "ETH_model.pkl")
data = pd.read_csv(DATA_PATH)
data.dropna(inplace=True)

#The features
features = ["price", "returns", "moving_avg_10", "moving_avg_50"]
X = data[features]
y = data["volatility"]

#Split the data stuff
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Training using random forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#Eval model & save
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")

joblib.dump(model, MODEL_PATH)