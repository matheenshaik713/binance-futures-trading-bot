from binance.client import Client
from config import API_KEY, SECRET_KEY
from config import BASE_URL, APP_MODE
from bot.logging_config import logger


class BinanceFuturesClient:


    def __init__(self):

        try:

            if APP_MODE == "DEMO":

                self.client = None
                logger.info(
                    "Running in DEMO mode"
                )

            else:

                self.client = Client(
                    API_KEY,
                    SECRET_KEY,
                    testnet=True
                )

                self.client.FUTURES_URL = BASE_URL

                logger.info(
                    "Connected to Binance Futures Testnet"
                )


        except Exception as e:

            logger.exception(
                "Failed to connect Binance"
            )

            raise e


    def get_client(self):

        return self.client