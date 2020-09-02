"""Plotly chart creation."""
import plotly.graph_objects as go
import chart_studio.plotly as py
from chart_studio.tools import set_credentials_file
from pandas import DataFrame
from config import PLOTLY_API_KEY, PLOTLY_USERNAME


set_credentials_file(
    username=PLOTLY_USERNAME,
    api_key=PLOTLY_API_KEY
)


def create_chart(stock_df: DataFrame, symbol: str) -> py.plot:
    """Create Plotly chart from Pandas DataFrame."""
    fig = go.Figure(data=[
        go.Candlestick(
            x=stock_df.index,
            open=stock_df['open'],
            high=stock_df['high'],
            low=stock_df['low'],
            close=stock_df['close'],
        )],
        layout=go.Layout(
            title=f'30-day performance of {symbol.upper()}',
            xaxis={
              'type': 'date',
              'rangeslider': {
                  'visible': False
              },
            },
        )
    )
    chart = py.plot(
        fig,
        filename=symbol,
        auto_open=False,
        fileopt='overwrite',
        sharing='public'
    )
    return chart
