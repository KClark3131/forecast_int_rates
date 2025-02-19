# Install necessary packages
!pip install fredapi pandas numpy matplotlib statsmodels

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fredapi import Fred
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# **Step 1: Fetch Real-Time Interest Rate Data from FRED**
FRED_API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your API key
fred = Fred(api_key=FRED_API_KEY)

# Fetch 30-Year Fixed Mortgage Rate Data
series_id = 'MORTGAGE30US'
real_time_rates = fred.get_series(series_id)

# Convert to DataFrame
df_real_time = real_time_rates.to_frame(name='30yr_FRM')
df_real_time.index = pd.to_datetime(df_real_time.index)
df_real_time.reset_index(inplace=True)
df_real_time.rename(columns={'index': 'Date'}, inplace=True)

# Plot real-time data
plt.figure(figsize=(12,6))
plt.plot(df_real_time['Date'], df_real_time['30yr_FRM'], label='Real-Time 30-Year FRM', color='blue')
plt.xlabel('Date')
plt.ylabel('Interest Rate (%)')
plt.title('Real-Time 30-Year Fixed Mortgage Rate')
plt.legend()
plt.grid(True)
plt.show()

# **Step 2: Load Historical Data**
file_path = "Cleaned_Interest_Rate_Data.csv"  # Ensure this file is in the working directory
df_historical = pd.read_csv(file_path, parse_dates=["Date"])

# Merge Real-Time Data with Historical Data
df_combined = pd.concat([df_historical, df_real_time]).drop_duplicates().sort_values(by="Date")

# **Step 3: Train Forecasting Models (ARIMA, SARIMA, ETS)**

# 1️⃣ **Fit ARIMA Model**
arima_order = (1,1,1)
arima_model = ARIMA(df_combined["30yr_FRM"], order=arima_order)
arima_result = arima_model.fit()
arima_forecast = arima_result.forecast(steps=12)  # Forecast next 12 months

# 2️⃣ **Fit SARIMA Model**
sarima_order = (1,1,1)
seasonal_order = (1,1,0,12)  # Monthly seasonality
sarima_model = SARIMAX(df_combined["30yr_FRM"], order=sarima_order, seasonal_order=seasonal_order)
sarima_result = sarima_model.fit()
sarima_forecast = sarima_result.forecast(steps=12)

# 3️⃣ **Fit Exponential Smoothing Model**
ets_model = ExponentialSmoothing(df_combined["30yr_FRM"], trend="add", seasonal=None, damped_trend=True)
ets_result = ets_model.fit()
ets_forecast = ets_result.forecast(steps=12)

# **Step 4: Create Forecast DataFrame**
forecast_dates = pd.date_range(start=df_combined["Date"].max(), periods=13, freq='M')[1:]
forecast_df = pd.DataFrame({
    "Date": forecast_dates,
    "ARIMA_Forecast": arima_forecast.values,
    "SARIMA_Forecast": sarima_forecast.values,
    "ETS_Forecast": ets_forecast.values
})

# **Step 5: Visualize Forecasts**
plt.figure(figsize=(12,6))
plt.plot(df_combined["Date"], df_combined["30yr_FRM"], label="Actual 30-Year FRM", color="blue")
plt.plot(forecast_df["Date"], forecast_df["ARIMA_Forecast"], label="ARIMA Forecast", color="red", linestyle="dashed")
plt.plot(forecast_df["Date"], forecast_df["SARIMA_Forecast"], label="SARIMA Forecast", color="purple", linestyle="dashdot")
plt.plot(forecast_df["Date"], forecast_df["ETS_Forecast"], label="ETS Forecast", color="green", linestyle="dotted")
plt.xlabel("Year")
plt.ylabel("Interest Rate (%)")
plt.title("Updated Forecasts with Real-Time Data (ARIMA vs SARIMA vs ETS)")
plt.legend()
plt.grid(True)
plt.show()

# Display updated forecast results
import ace_tools as tools
tools.display_dataframe_to_user(name="Updated Forecast with Real-Time Data", dataframe=forecast_df)
