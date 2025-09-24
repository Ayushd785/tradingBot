# trading_bot/cli.py
import argparse
from .bot import BasicBot

def run():
    """Parses command-line arguments and executes the corresponding bot action."""
    parser = argparse.ArgumentParser(description="A simplified Binance trading bot.")
    
    parser.add_argument("order_type", help="Type of order", choices=['market', 'limit', 'stop-limit'])
    parser.add_argument("symbol", help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("side", help="Order side", choices=['buy', 'sell'])
    parser.add_argument("quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for limit orders)")
    parser.add_argument("--stop-price", type=float, help="Stop price (required for stop-limit orders)")

    args = parser.parse_args()

    if args.order_type == 'limit' and not args.price:
        parser.error("--price is required for limit orders.")
    
    if args.order_type == 'stop-limit' and not getattr(args, 'stop_price', None):
        parser.error("--stop-price is required for stop-limit orders.")

    bot = BasicBot()

    if args.order_type == 'market':
        bot.place_market_order(args.symbol, args.side, args.quantity)
    elif args.order_type == 'limit':
        bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)
    elif args.order_type == 'stop-limit':
        bot.place_stop_limit_order(args.symbol, args.side, args.quantity, args.price, getattr(args, 'stop_price', None))