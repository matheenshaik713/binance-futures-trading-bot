import streamlit as st
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

st.set_page_config(
    page_title="Binance Futures Trading Bot",
    page_icon="📈",
    layout="centered"
)

with st.sidebar:

    st.title("Bot Status")

    st.success("Connected")

    st.markdown("---")

    st.write("Environment")

    st.info("Binance Futures Testnet")

    st.markdown("---")

    st.write("Developer")

    st.write("Shaik Mateen")

st.title("📈 Binance Futures Testnet Trading Bot")

st.markdown("---")

symbol = st.selectbox(
    "Trading Symbol",
    ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
)

side = st.radio(
    "Order Side",
    ["BUY", "SELL"],
    horizontal=True
)

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001,
    step=0.001,
    format="%.3f"
)

price = None

if order_type == "LIMIT":

    price = st.number_input(
        "Limit Price",
        min_value=1.0,
        value=50000.0,
        step=100.0
    )

st.markdown("---")

if st.button("🚀 Place Order", use_container_width=True):

    try:

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            price = validate_price(price)

        client = BinanceFuturesClient().get_client()

        manager = OrderManager(client)

        if order_type == "MARKET":

            response = manager.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = manager.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        st.success("Order Submitted Successfully")

        st.markdown("## Order Request")

        st.write({
            "Symbol": symbol,
            "Side": side,
            "Order Type": order_type,
            "Quantity": quantity,
            "Price": price if order_type == "LIMIT" else "-"
        })

        st.markdown("## Order Response")

        st.success("Order Submitted Successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Order ID", response.get("orderId"))

        with col2:
            st.metric("Status", response.get("status"))

        col3, col4 = st.columns(2)

        with col3:
            st.metric("Executed Qty", response.get("executedQty"))

        with col4:
            st.metric("Type", response.get("type"))

    except Exception as e:

        st.error(str(e))

st.markdown("---")

st.subheader("Application Logs")

try:

    with open("logs/trading.log", "r") as file:

        logs = file.read()

    st.text_area(
        "Logs",
        logs,
        height=250
    )

except FileNotFoundError:

    st.info("No logs available.")