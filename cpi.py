import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data
data = pd.read_excel('CPI.xlsx')

# Calculate the actual ∆cpit series
data["CPI Change"] = data["CPI"].diff()

# Select the appropriate sample
sample = data

# Define the ARIMA model
model = sm.tsa.statespace.SARIMAX(sample["CPI"], order=(1, 1, 1), seasonal_order=(1, 1, 0, 12))

# Estimate the model
results = model.fit()

# Generate forecasts
start = pd.to_datetime("2022-01-01")
end = pd.to_datetime("2023-08-31")
forecasts = results.forecast(start, end)

# Plot the actual and forecast series
plt.plot(sample["Date"], sample["CPI Change"], label="Actual")
plt.plot(forecasts.index, forecasts, label="Forecast")
plt.legend()
plt.show()
