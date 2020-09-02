"""Configuration via environment variables."""
from os import environ, path
from dotenv import load_dotenv


# Load values from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# API
IEX_API_TOKEN = environ.get('IEX_API_TOKEN')
IEX_API_BASE_URL = 'https://cloud.iexapis.com/stable/stock/'

# Plotly
PLOTLY_API_KEY = environ.get('PLOTLY_API_KEY')
PLOTLY_USERNAME = environ.get('PLOTLY_USERNAME')

