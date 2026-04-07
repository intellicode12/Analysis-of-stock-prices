def add_moving_averages(df):
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    return df

def add_daily_returns(df):
    df['Daily Return'] = df['Close'].pct_change()
    return df

def add_volatility(df):
    df['Volatility'] = df['Daily Return'].rolling(window=20).std()
    return df
