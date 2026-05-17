import plotly.graph_objects as go

def create_stock_chart(df, ticker):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Close'],
            mode='lines',
            name='Close Price'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['MA_20'],
            mode='lines',
            name='20 Day Moving Average'
        )
    )

    fig.update_layout(
        title=f"{ticker} Stock Analysis",
        xaxis_title="Date",
        yaxis_title="Price"
    )

    return fig