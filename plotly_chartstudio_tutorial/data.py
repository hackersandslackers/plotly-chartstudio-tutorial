"""Parse raw data into Pandas DataFrame."""
import pandas as pd


def parse_data(data) -> pd.DataFrame:
    """Parse JSON as Pandas DataFrame."""
    stock_df = pd.read_json(data)
    stock_df = stock_df.loc[stock_df['date'].dt.dayofweek < 5]
    stock_df.set_index(keys=stock_df['date'], inplace=True)
    return stock_df
