import yfinance as yf

def get_stock_data(ticker):

    stock = yf.Ticker(ticker)

    df = stock.history(period="1y")

    df['MA_20'] = df['Close'].rolling(20).mean()

    df['Returns'] = df['Close'].pct_change()

    return df