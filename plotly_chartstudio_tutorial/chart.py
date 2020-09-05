"""Plotly chart creation."""
import plotly.graph_objects as go
import chart_studio.plotly as py
from chart_studio.tools import set_credentials_file
from pandas import DataFrame
from config import PLOTLY_API_KEY, PLOTLY_USERNAME

# Plotly Chart Studio authentication
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
            decreasing={
                "line": {
                    "color": "rgb(240, 99, 90)"
                },
                "fillcolor": "rgba(142, 53, 47, 0.5)"
            },
            increasing={
                "line": {
                    "color": "rgb(48, 190, 161)"
                },
                "fillcolor": "rgba(22, 155, 124, 0.6)"
            },
            whiskerwidth=1,
        )],
        layout=go.Layout(
            font={
                "size": 15,
                "family": "Open Sans",
                "color": "#fff"
            },
            title={
                "x": 0.5,
                "font": {"size": 23},
                "text": f'30-day performance of {symbol.upper()}'
            },
            xaxis={
                'type': 'date',
                'rangeslider': {
                    'visible': False
                },
                "ticks": "",
                "gridcolor": "#283442",
                "linecolor": "#506784",
                "automargin": True,
                "zerolinecolor": "#283442",
                "zerolinewidth": 2
            },
            yaxis={
                "ticks": "",
                "gridcolor": "#283442",
                "linecolor": "#506784",
                "automargin": True,
                "zerolinecolor": "#283442",
                "zerolinewidth": 2
            },
            autosize=True,
            plot_bgcolor="rgb(23, 27, 31)",
            paper_bgcolor="rgb(23, 27, 31)",
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
