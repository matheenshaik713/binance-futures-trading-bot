class TradingBotException(Exception):
    """Base exception for Trading Bot."""
    pass


class ValidationError(TradingBotException):
    pass


class BinanceConnectionError(TradingBotException):
    pass