"""Initialize script."""
from .api import fetch_stock_data
from .data import parse_data
from .chart import create_chart
from .log import logger


def init_script() -> str:
    """Create candlestick chart in Plotly Chart Studio."""
    symbol = "NET"
    raw_data = fetch_stock_data(symbol)
    parsed_data = parse_data(raw_data)
    plot_url = create_chart(parsed_data, symbol)
    logger.info(plot_url)
    return plot_url
