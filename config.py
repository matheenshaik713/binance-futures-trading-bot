import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except ImportError:
    st = None


def get_secret(key):

    # Streamlit Cloud secrets
    if st is not None:
        try:
            return st.secrets[key]
        except Exception:
            pass

    # Local .env
    return os.getenv(key)


API_KEY = get_secret("BINANCE_API_KEY")
SECRET_KEY = get_secret("BINANCE_SECRET_KEY")

BASE_URL = "https://testnet.binancefuture.com"


if not API_KEY or not SECRET_KEY:
    raise ValueError(
        "API credentials not found. Add them in Streamlit Secrets or .env"
    )