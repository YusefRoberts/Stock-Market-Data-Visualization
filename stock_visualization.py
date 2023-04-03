import yfinance as yf
import plotly.graph_objs as go

# Prompt the user for a ticker symbol, start date, and end date
ticker = input("Enter a ticker symbol: ")
start_date = input("Enter a start date (YYYY-MM-DD): ")
end_date = input("Enter an end date (YYYY-MM-DD): ")

# Fetch data for the specified ticker symbol and date range
df = yf.download(ticker, start=start_date, end=end_date)

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Show the chart
fig.show()
