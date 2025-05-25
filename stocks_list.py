import pandas as pd

# Read the first CSV file into 'daily_stocks'
daily_stocks = pd.read_csv('D:\Backtest\Momenrum Burst\Daily\Backtest Daily Stock Data, Technical Analysis Scanner (9).csv')

# Read the second CSV file into 'volume_stocks'
volume_stocks = pd.read_csv('D:\Backtest\Momenrum Burst\Daily\Backtest Copy - HVY @finallynitin, Technical Analysis Scanner (4).csv')

daily_stocks['Date'] = pd.to_datetime(daily_stocks['date'], errors='coerce', dayfirst=True).fillna(
    pd.to_datetime(daily_stocks['date'], errors='coerce', format='%Y-%m-%d')
).dt.strftime('%Y-%m-%d')

volume_stocks['Date'] = pd.to_datetime(volume_stocks['date'], errors='coerce', dayfirst=True).fillna(
    pd.to_datetime(volume_stocks['date'], errors='coerce', format='%Y-%m-%d')
).dt.strftime('%Y-%m-%d')

# Ensure 'Date' column is in datetime format
volume_stocks['Date'] = pd.to_datetime(volume_stocks['Date'])

# Filter for March, April, and May
volume_stocks_filtered = volume_stocks[volume_stocks['Date'].dt.month.isin([3, 4, 5])]
volume_stocks = volume_stocks.sort_values(by=['symbol', 'Date'], ascending=[True, False])
volume_stocks['CumulativeCount'] = volume_stocks.groupby('symbol').cumcount() + 1

latest_per_stock = volume_stocks.groupby('symbol').tail(1).reset_index(drop=True)


daily_stocks['Date'] = pd.to_datetime(daily_stocks['Date'])

latest_date = daily_stocks['Date'].max()

latest_daily_data = daily_stocks[daily_stocks['Date'] == latest_date].sort_values(by='Date', ascending=False).reset_index(drop=True)
merged_df = pd.merge(
    latest_daily_data,
    latest_per_stock,
    on='symbol',
    how='left',
    suffixes=('_daily', '_volume')  # Optional: to handle overlapping column names
)
merged_df.to_csv('2025-05-23.csv')
