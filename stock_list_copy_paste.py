import pandas as pd
# df = pd.read_csv(r'D:\Backtest\Momenrum Burst\Daily\2025-05-23.csv')
# #print(df)
# df = df[(df['cumulative_sum'] >= 2) & (df['date_x'] == '2025-05-23')]
# #print(df)
# # df['date'] = pd.to_datetime(df['date'])
# # df['dat_1'] = df['date'].dt.date
# # df = df[df['date'] == '14-10-2024']
# #print(df)
# stokcs = set(df['symbol'])
# df = pd.DataFrame(stokcs, columns=['symbol'])
# df.to_csv('chartlink_2025-05-23.csv')
# formatted_symbols = ['NSE:' + i + '-EQ' for i in stokcs]

# formatted = pd.DataFrame(formatted_symbols, columns=['symbol'])
# with open("fyers_watchlist_2025-05-23.txt", "w") as f:
#     f.write("\n".join(formatted_symbols))



# Set the date once here
date = '2025-05-23'

# Load CSV
df = pd.read_csv(fr'D:\Backtest\Momenrum Burst\Daily\{date}.csv')
date = '23-05-2025'
# Filter rows based on cumulative_sum and date_x
df = df[(df['CumulativeCount'] >= 2) & (df['date_daily'] == date)]

# Get unique stock symbols
stocks = set(df['symbol'])

# Create DataFrame from the symbols and export to CSV
df_symbols = pd.DataFrame(stocks, columns=['symbol'])
df_symbols.to_csv(f'chartlink_{date}.csv', index=False)

# Format symbols for Fyers watchlist
formatted_symbols = ['NSE:' + symbol + '-EQ' for symbol in stocks]

# Save to watchlist text file
with open(f"fyers_watchlist_{date}.txt", "w") as f:
    f.write("\n".join(formatted_symbols))
