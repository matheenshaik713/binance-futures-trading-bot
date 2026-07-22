import typer
from rich import print

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

app = typer.Typer()


@app.command()
def trade(
    symbol: str = typer.Option(..., help="Trading symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., "--order-type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price (required for LIMIT orders)"),
):
    try:
        # Validate Inputs
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            price = validate_price(price)
            if price is None:
                raise ValueError("Price is required for LIMIT orders.")

        # Display Order Summary
        print("\n" + "=" * 50)
        print("[bold cyan]ORDER REQUEST[/bold cyan]")
        print("=" * 50)
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if order_type == "LIMIT":
            print(f"Price       : {price}")

        # Optional confirmation (Bonus UX)
        if not typer.confirm("\nDo you want to place this order?"):
            print("[yellow]Order cancelled by user.[/yellow]")
            raise typer.Exit()

        # Create Client
        client = BinanceFuturesClient().get_client()

        # Create Order Manager
        manager = OrderManager(client)

        # Place Order
        if order_type == "MARKET":
            response = manager.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
            )
        else:
            response = manager.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
            )

        # Display Response
        print("\n" + "=" * 50)
        print("[bold green]ORDER RESPONSE[/bold green]")
        print("=" * 50)

        print(f"Order ID      : {response.get('orderId', 'N/A')}")
        print(f"Status        : {response.get('status', 'N/A')}")
        print(f"Symbol        : {response.get('symbol', 'N/A')}")
        print(f"Side          : {response.get('side', 'N/A')}")
        print(f"Type          : {response.get('type', 'N/A')}")
        print(f"Executed Qty  : {response.get('executedQty', 'N/A')}")
        print(f"Average Price : {response.get('avgPrice', 'N/A')}")

        print("\n[bold green]✅ Order submitted successfully![/bold green]")

    except Exception as e:
        print("\n[bold red]❌ ORDER FAILED[/bold red]")
        print(f"Reason: {e}")


if __name__ == "__main__":
    app()