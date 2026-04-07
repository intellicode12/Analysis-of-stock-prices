import yfinance as yf

def get_stock_data(ticker, start="2022-01-01", end="2024-01-01"):
    df = yf.download(ticker, start=start, end=end)
    df.dropna(inplace=True)
    return df
