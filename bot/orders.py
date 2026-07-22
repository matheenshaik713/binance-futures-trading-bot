from binance.exceptions import BinanceAPIException
from bot.logging_config import logger
from config import APP_MODE
import random


class OrderManager:

    def __init__(self, client):
        self.client = client


    def place_market_order(self, symbol, side, quantity):

        try:

            logger.info(
                f"MARKET ORDER -> {symbol} {side} Qty:{quantity}"
            )


            # Demo mode for Streamlit Cloud
            if APP_MODE == "DEMO":

                response = {
                    "orderId": random.randint(100000000, 999999999),
                    "symbol": symbol,
                    "status": "FILLED",
                    "type": "MARKET",
                    "side": side,
                    "executedQty": str(quantity),
                    "avgPrice": "Demo Price"
                }

                logger.info(
                    f"DEMO RESPONSE: {response}"
                )

                return response


            # Real Binance Testnet Order
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )


            logger.info(
                f"Response: {response}"
            )

            return response


        except BinanceAPIException as e:

            logger.error(
                f"Binance API Error: {e}"
            )

            raise


        except Exception as e:

            logger.exception(e)

            raise



    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price,
    ):

        try:

            logger.info(
                f"LIMIT ORDER -> {symbol} {side} Qty:{quantity} Price:{price}"
            )


            # Demo mode for Streamlit Cloud
            if APP_MODE == "DEMO":

                response = {
                    "orderId": random.randint(100000000, 999999999),
                    "symbol": symbol,
                    "status": "NEW",
                    "type": "LIMIT",
                    "side": side,
                    "executedQty": "0",
                    "price": str(price)
                }


                logger.info(
                    f"DEMO RESPONSE: {response}"
                )

                return response



            # Real Binance Testnet Order
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )


            logger.info(
                f"Response: {response}"
            )

            return response



        except BinanceAPIException as e:

            logger.error(
                f"Binance API Error: {e}"
            )

            raise


        except Exception as e:

            logger.exception(e)

            raise