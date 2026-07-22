from binance.client import Client
from config import API_KEY, SECRET_KEY
from bot.logging_config import logger


class BinanceFuturesClient:
    def __init__(self):
        try:
            self.client = Client(
                API_KEY,
                SECRET_KEY,
                testnet=True
            )

            logger.info("Connected to Binance Testnet")

        except Exception as e:
            logger.exception(e)
            raise

    def get_client(self):
        return self.client