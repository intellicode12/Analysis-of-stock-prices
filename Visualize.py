import matplotlib.pyplot as plt

def plot_stock(df, ticker):
    plt.figure()
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['MA50'], label='50-Day MA')
    plt.plot(df['MA200'], label='200-Day MA')

    plt.title(f"{ticker} Stock Price Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()

    plt.show()

def plot_returns(df):
    plt.figure()
    plt.plot(df['Daily Return'])
    plt.title("Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Return")
    plt.grid()
    plt.show()

def plot_volatility(df):
    plt.figure()
    plt.plot(df['Volatility'])
    plt.title("Volatility (20-day rolling)")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.grid()
    plt.show()
