# this script will be used to scrape financial data from Yahoo Finance for lemonade inc stocks to then generate a ML model to predict stock prices
import yfinance as yf
from datetime import datetime, timedelta
ticker = "ROOT"
end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)  # approx last 5 years
# download daily OHLCV
data = yf.download(
    ticker,
    start=start_date.strftime("%Y-%m-%d"),
    end=end_date.strftime("%Y-%m-%d"),
    interval="1d",
    auto_adjust=False,   # keeping raw data here 
)

# reset index so Date becomes a column
data = data.reset_index()

# save to CSV
output_path = "Data/root_daily_5y.csv"
data.to_csv(output_path, index=False)
print(f"Saved {len(data)} rows to {output_path}")