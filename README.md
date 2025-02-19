# Interest Rate Forecasting using ARIMA, SARIMA, and Exponential Smoothing

## Overview
This project integrates **real-time interest rate data** from the **Federal Reserve Economic Data (FRED) API** and combines it with historical mortgage rate data to generate forecasts using **ARIMA, SARIMA, and Exponential Smoothing (ETS) models**.

## Features
✅ Fetches **real-time 30-year fixed mortgage rates** from the FRED API  
✅ Cleans and integrates **historical and real-time data**  
✅ Fits **three forecasting models**: ARIMA, SARIMA, and ETS  
✅ **Generates 12-month forecasts** with comparative visualization  
✅ **Displays forecast results** for further analysis  

## Prerequisites
To run this project, you need:
- Python 3.x
- API key from [FRED](https://fred.stlouisfed.org/)
- Installed dependencies:
  ```bash
  pip install fredapi pandas numpy matplotlib statsmodels
  ```

## Usage
### Step 1: Get FRED API Key
1. **Register at** [FRED API](https://fred.stlouisfed.org/)
2. **Obtain an API Key** (sent via email)
3. **Replace** `'YOUR_API_KEY_HERE'` in the script with your API key

### Step 2: Run the Forecasting Script
1. **Ensure your historical data is available** (`Cleaned_Interest_Rate_Data.csv`)
2. **Run the Python script**
3. **View forecasts** in the displayed output and visualizations

## Key Functions
### 1. Fetch Real-Time Data
- Retrieves **30-year fixed mortgage rates** using the FRED API.

### 2. Data Cleaning & Merging
- Combines real-time data with historical records.

### 3. Forecasting Models
- **ARIMA** (Auto-Regressive Integrated Moving Average)
- **SARIMA** (Seasonal ARIMA)
- **Exponential Smoothing (ETS)**

### 4. Visualization
- **Compares** model forecasts
- **Plots** actual vs predicted trends

## Expected Output
- A **forecast table** with predictions for the next **12 months**
- A **visual comparison** of ARIMA, SARIMA, and ETS models

## Example Forecast Output
| Date       | ARIMA Forecast | SARIMA Forecast | ETS Forecast |
|------------|---------------|----------------|-------------|
| 2025-03-31 | 6.88          | 6.90           | 6.85        |
| 2025-04-30 | 6.86          | 6.92           | 6.84        |

## Next Steps
🚀 **Enhance the model** with hyperparameter tuning  
📊 **Test alternative forecasting methods** (e.g., LSTM, Prophet)  
🔍 **Incorporate economic indicators** for deeper insights  

## License
This project is open-source and free to use.

## Questions?
Feel free to ask for support or improvements!

