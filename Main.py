from src.fetch_data import get_stock_data
from src.analysis import add_moving_averages, add_daily_returns, add_volatility
from src.visualize import plot_stock, plot_returns, plot_volatility

def main():
    ticker = "AAPL"  # Change to any stock (e.g., TSLA, MSFT, RELIANCE.NS)

    print(f"Fetching data for {ticker}...")

    df = get_stock_data(ticker)

    print("Analyzing data...")
    df = add_moving_averages(df)
    df = add_daily_returns(df)
    df = add_volatility(df)

    print("Generating plots...")
    plot_stock(df, ticker)
    plot_returns(df)
    plot_volatility(df)

if __name__ == "__main__":
    main()
