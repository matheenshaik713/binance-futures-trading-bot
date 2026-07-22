import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except:
    st = None


def get_secret(key):

    if st:
        try:
            return st.secrets[key]
        except:
            pass

    return os.getenv(key)


API_KEY = get_secret("BINANCE_API_KEY")
SECRET_KEY = get_secret("BINANCE_SECRET_KEY")

BASE_URL = "https://testnet.binancefuture.com"


# Deployment mode
APP_MODE = get_secret("APP_MODE") or "LIVE"