"""Fetch data from third-party API."""
import requests
from config import IEX_API_BASE_URL, IEX_API_TOKEN


def fetch_stock_data(stock_symbol: str):
    """Fetch stock data from API"""
    params = {'token': IEX_API_TOKEN, 'includeToday': 'true'}
    url = f'{IEX_API_BASE_URL}/{stock_symbol}/chart/1m'
    req = requests.get(url, params=params)
    data = req.content
    return data
