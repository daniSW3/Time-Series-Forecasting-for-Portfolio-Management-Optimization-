Task 1: Data Preprocessing and Exploratory Data Analysis (EDA)
Overview
This task involves preprocessing and analyzing historical financial data for three assets: Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY) from July 1, 2015, to July 31, 2025. The data, sourced from Yahoo Finance using the yfinance library, includes daily metrics (Open, High, Low, Close, Adj Close, Volume, Daily Return, Volatility). The preprocessing ensures data quality, while the EDA identifies trends, volatility, stationarity, outliers, and risk metrics to prepare for time series forecasting and portfolio optimization.
Objectives

Data Cleaning: Load data, convert to appropriate types, handle missing values, and normalize for machine learning.
Exploratory Data Analysis:
Visualize closing prices and daily returns to identify trends and volatility.
Perform stationarity tests (Augmented Dickey-Fuller) to assess modeling requirements.
Detect outliers in daily returns.
Calculate risk metrics (Value at Risk, Sharpe Ratio) for portfolio insights.


Output: Generate cleaned datasets and visualizations for further analysis.

Project Structure
The relevant files for Task 1 are located in the project directory:
Time Series Forecasting for Portfolio Management Optimization/
├── financial_data/
│   ├── TSLA_historical_data_2015_2025.csv
│   ├── BND_historical_data_2015_2025.csv
│   ├── SPY_historical_data_2015_2025.csv
│   ├── TSLA_cleaned_data_2015_2025.csv
│   ├── BND_cleaned_data_2015_2025.csv
│   ├── SPY_cleaned_data_2015_2025.csv
├── eda_plots/
│   ├── TSLA_close_price.png
│   ├── TSLA_daily_returns.png
│   ├── TSLA_rolling_stats.png
│   ├── BND_close_price.png
│   ├── BND_daily_returns.png
│   ├── BND_rolling_stats.png
│   ├── SPY_close_price.png
│   ├── SPY_daily_returns.png
│   ├── SPY_rolling_stats.png
├── fetch_financial_data.py
├── preprocess_and_eda_fixed_seaborn.py
├── .gitignore
└── README.md

Setup

Clone the Repository (if applicable):git clone <repository_url>
cd "Time Series Forecasting for Portfolio Management Optimization"


Create and Activate Virtual Environment:python -m venv wk11
wk11\Scripts\Activate


Install Dependencies:pip install pandas numpy matplotlib seaborn statsmodels scikit-learn yfinance


Verify Data:Ensure the financial_data directory contains the raw CSV files (TSLA_historical_data_2015_2025.csv, etc.). If missing, run:python fetch_financial_data.py



Running the Script
Execute the preprocessing and EDA script:
python preprocess_and_eda_fixed_seaborn.py

Outputs

Cleaned Data: Saved as financial_data/{ticker}_cleaned_data_2015_2025.csv for each ticker (TSLA, BND, SPY).
Visualizations: Plots saved in eda_plots/:
{ticker}_close_price.png: Adjusted Close price over time.
{ticker}_daily_returns.png: Daily percentage returns.
{ticker}_rolling_stats.png: Adjusted Close with 21-day rolling mean and standard deviation.


Console Output: Statistics, stationarity test results, outlier counts, and risk metrics.

Key Insights from EDA
Data Cleaning

Data Types:
Initial data had Open, High, Low, Close, Adj Close, and Volume as object (strings), converted to float64 using pd.to_numeric.
Daily_Return and Volatility were already float64.


Missing Values:
Each dataset had 1 missing value per column, handled by linear interpolation for prices and forward fill for Volume, Daily_Return, and Volatility.
Note: The output shows missing values persisting after cleaning, indicating a potential issue in the interpolation logic (to be fixed in future iterations by ensuring proper data alignment).



Basic Statistics

TSLA:
Mean Adj Close: $132.92, with a high standard deviation ($120.97), reflecting high volatility.
Daily returns: Mean 0.19%, standard deviation 3.75%, indicating significant daily fluctuations.
Volume: Mean 114.67M shares, with peaks up to 914.08M.


BND:
Mean Adj Close: $68.53, with low standard deviation ($4.52), confirming stability.
Daily returns: Near-zero mean (-0.002%), low standard deviation (0.35%), typical for bonds.
Volume: Mean 4.46M units, lower than equities.


SPY:
Mean Adj Close: $335.51, with moderate standard deviation ($126.13), reflecting diversified market exposure.
Daily returns: Mean 0.05%, standard deviation 1.18%, indicating moderate volatility.
Volume: Mean 84.81M shares, with peaks up to 507.24M.



Stationarity (ADF Test)

TSLA:
Adj Close: Non-stationary (p-value = 0.5713 > 0.05). Requires differencing for ARIMA modeling.
Daily_Return: Stationary (p-value = 0.0000 < 0.05), suitable for time series models.


BND:
Adj Close: Non-stationary (p-value = 0.5432 > 0.05). Requires differencing.
Daily_Return: Stationary (p-value = 0.0000 < 0.05).


SPY:
Adj Close: Non-stationary (p-value = 0.9889 > 0.05). Requires differencing.
Daily_Return: Stationary (p-value = 0.0000 < 0.05).



Outlier Detection

TSLA: 90 days with outliers in Daily_Return (e.g., -9% on 2015-08-06, +11% on 2015-11-04), reflecting high volatility due to news or earnings.
BND: 242 days with outliers, but smaller in magnitude (e.g., ±1%), consistent with low-risk bonds.
SPY: 198 days with outliers (e.g., -4% on 2015-08-24), tied to market-wide events.

Risk Metrics

TSLA:
95% VaR: -5.00% (5% chance of losing more than 5% in a day), indicating high risk.
Sharpe Ratio: 0.7823, suggesting decent risk-adjusted returns but driven by high volatility.


BND:
95% VaR: 0.00% (negligible daily loss risk), reflecting stability.
Sharpe Ratio: -0.4523, negative due to near-zero returns relative to the risk-free rate (2%).


SPY:
95% VaR: -2.00% (5% chance of losing more than 2% in a day), moderate risk.
Sharpe Ratio: 0.6252, indicating solid risk-adjusted returns for diversified exposure.



Trends and Volatility

TSLA: Strong upward trend in Adj Close, with significant volatility spikes (e.g., max volatility 155%). High daily return fluctuations impact portfolio risk.
BND: Stable Adj Close with minimal fluctuations, low volatility (max 31%), suitable for risk-averse portfolios.
SPY: Steady upward trend, moderate volatility (max 93%), balancing growth and stability.

Notes

FutureWarning: The script uses DataFrame.fillna(method='ffill'), which is deprecated. Future versions should use df.ffill() to avoid warnings.
Missing Values Issue: The cleaning process did not fully resolve missing values (1 per column remains). This may require revisiting the clean_data function to ensure proper handling (e.g., checking for edge cases or re-running data fetching).
Visualizations: Plots in eda_plots/ show trends, daily returns, and rolling statistics, aiding in identifying patterns for forecasting.

Next Steps

Fix missing value handling in clean_data to ensure no NaNs remain.
Perform correlation analysis between assets for portfolio optimization.
Proceed to time series forecasting (e.g., ARIMA) using differenced Adj Close or stationary Daily_Return.
