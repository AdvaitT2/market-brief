"""
data.py — fetches daily share prices from Alpha Vantage.

Week 1: you don't need to understand this file. Just import it and use it:

    from data import get_daily_prices
    df = get_daily_prices("AAPL")

Week 2: you WILL need to understand it, because you're going to rewrite it
from scratch. Feel free to read it now and write down any questions.
"""

import os
import sys

import pandas as pd
import requests
from dotenv import load_dotenv

# Reads the .env file in this folder and makes its contents available
# via os.getenv(). This is how we keep the API key out of the code.
load_dotenv()

BASE_URL = "https://www.alphavantage.co/query"

# Alpha Vantage names its columns like "1. open" and "4. close".
# We rename them to something sane.
COLUMN_NAMES = {
    "1. open": "open",
    "2. high": "high",
    "3. low": "low",
    "4. close": "close",
    "5. volume": "volume",
}


class DataError(Exception):
    """Raised when we can't get usable data back from the API."""


def load_example_prices():
    """Return practice data from example_prices.csv — no internet needed.

    This gives you a DataFrame in exactly the same shape as
    get_daily_prices() does, so anything you build on top of one will work
    on the other. Handy for getting started, and for working on a train.

    Note: this file contains made-up numbers for practice. They are not
    real prices for any real company.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(here, "example_prices.csv")
    return pd.read_csv(csv_path, index_col="date", parse_dates=True)


def get_daily_prices(symbol, days=90):
    """Return a DataFrame of daily prices for one ticker symbol.

    Args:
        symbol: ticker symbol, e.g. "AAPL", "MSFT", "TSLA".
        days: how many of the most recent trading days to return.

    Returns:
        A pandas DataFrame, oldest row first, with a DatetimeIndex named
        "date" and the columns: open, high, low, close, volume.

    Raises:
        DataError: if the key is missing, the symbol is unknown, or the
            API says something we didn't expect.
    """
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    if not api_key:
        raise DataError(
            "No API key found. Copy .env.example to .env and put the key in it."
        )

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        # "compact" gives the latest 100 days, "full" gives 20+ years.
        "outputsize": "compact" if days <= 100 else "full",
        "apikey": api_key,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=30)
        response.raise_for_status()
    except requests.RequestException as error:
        raise DataError(f"Could not reach Alpha Vantage: {error.__class__.__name__}") from error
    payload = response.json()

    # Alpha Vantage returns HTTP 200 even when something went wrong,
    # so we have to inspect the body to find out.
    if "Error Message" in payload:
        raise DataError(f"API rejected symbol {symbol!r}: {payload['Error Message']}")
    if "Note" in payload or "Information" in payload:
        raise DataError(f"API refused the request: {payload.get('Note') or payload['Information']}")

    table = payload.get("Time Series (Daily)")
    if not table:
        raise DataError(f"No price data in the response. Got keys: {list(payload)}")

    df = pd.DataFrame.from_dict(table, orient="index")
    df = df.rename(columns=COLUMN_NAMES)
    df = df.astype(float)
    df["volume"] = df["volume"].astype("int64")

    # The API gives newest-first with string dates. We want oldest-first
    # with real dates, so that plotting left-to-right means past-to-present.
    df.index = pd.to_datetime(df.index)
    df.index.name = "date"
    df = df.sort_index()

    return df.tail(days)


def _self_check(symbol="AAPL"):
    """Run me before you write any code, to prove your setup works."""
    print(f"Asking Alpha Vantage for {symbol}...")
    df = get_daily_prices(symbol, days=5)
    print(f"\nGot {len(df)} rows. Here they are:\n")
    print(df)
    print(f"\nColumns available: {list(df.columns)}")
    print("Setup works. You're ready to start.")


if __name__ == "__main__":
    # Lets you run:  python data.py        (checks AAPL)
    #           or:  python data.py MSFT   (checks MSFT)
    requested = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    try:
        _self_check(requested)
    except DataError as error:
        print(f"\nSomething's not right: {error}")
        sys.exit(1)
