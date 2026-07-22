from binance.exceptions import BinanceAPIException
from bot.logging_config import logger


class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):

        try:

            logger.info(
                f"MARKET ORDER -> {symbol} {side} Qty:{quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

            logger.info(response)

            return response

        except BinanceAPIException as e:
            logger.error(e.message)
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

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

            logger.info(f"Response: {response}")
            

            return response

        except BinanceAPIException as e:
            logger.error(e.message)
            raise

        except Exception as e:
            logger.exception(e)
            raise