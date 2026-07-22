from bot.exceptions import ValidationError


def validate_symbol(symbol: str):

    if len(symbol) < 6:
        raise ValidationError("Invalid symbol.")

    return symbol.upper()


def validate_side(side: str):

    side = side.upper()

    if side not in ("BUY", "SELL"):
        raise ValidationError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str):

    order_type = order_type.upper()

    if order_type not in ("MARKET", "LIMIT"):
        raise ValidationError(
            "Order type must be MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity):

    try:
        quantity = float(quantity)
    except ValueError:
        raise ValidationError("Quantity must be numeric.")

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero."
        )

    return quantity


def validate_price(price):

    if price is None:
        return None

    try:
        price = float(price)
    except ValueError:
        raise ValidationError("Price must be numeric.")

    if price <= 0:
        raise ValidationError("Price must be positive.")

    return price