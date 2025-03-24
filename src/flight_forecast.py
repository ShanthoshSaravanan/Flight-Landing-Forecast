import pandas as pd
import joblib
import matplotlib.pyplot as plt
from transformers import pipeline
from sklearn.linear_model import LinearRegression

# ✅ Load Dataset
data = {
    "Activity_Period": [2020, 2021, 2022, 2023, 2024],
    "Landing_Count": [5000, 5200, 4800, 5100, 5300]
}
df = pd.DataFrame(data)

# ✅ Train Forecasting Model (Simple Linear Regression)
X = df["Activity_Period"].values.reshape(-1, 1)
y = df["Landing_Count"].values
model = LinearRegression()
model.fit(X, y)

# ✅ Predict Next 2 Years
future_years = [[2025], [2026]]
predictions = model.predict(future_years)
df_pred = pd.DataFrame({"Activity_Period": [2025, 2026], "Landing_Count": predictions})

# ✅ Save Model
joblib.dump(model, "models/flight_forecast.pkl")

# ✅ AI-Based Analysis (LLM)
llm_pipeline = pipeline("text-generation", model="distilgpt2")
data_summary = df.to_string(index=False)
prompt = f"""
The following table shows historical flight landing data:

{data_summary}

Predict the trend for the next 2 years, considering seasonality, anomalies, and growth patterns.
"""
result = llm_pipeline(prompt, max_length=300, truncation=True)[0]["generated_text"]

# ✅ Save LLM Insights
with open("models/flight_llm.txt", "w") as f:
    f.write(result)

# ✅ Visualization
plt.figure(figsize=(8, 5))
plt.plot(df["Activity_Period"], df["Landing_Count"], marker='o', label="Historical Data")
plt.plot(df_pred["Activity_Period"], df_pred["Landing_Count"], marker='x', linestyle="dashed", color="red", label="Forecasted Data")
plt.xlabel("Year")
plt.ylabel("Landing Count")
plt.legend()
plt.title("Flight Landing Forecast")
plt.savefig("reports/predictions_chart.png")
plt.show()

# ✅ Print AI Insights
print("\n🔍 AI-Generated Trend Analysis & Forecast:\n")
print(result)
