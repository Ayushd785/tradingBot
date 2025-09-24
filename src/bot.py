# trading_bot/bot.py
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Import the configured API keys
from . import config

class BasicBot:
    def __init__(self):
        """Initializes the bot by loading credentials from the config file."""
        self.client = Client(
            api_key=config.API_KEY, 
            api_secret=config.API_SECRET, 
            testnet=True  # TESTNET - FAKE MONEY
        )
        logging.info("Bot initialized using configured API key.")

    def place_market_order(self, symbol, side, quantity):
        """Places a market order."""
        try:
            logging.info(f"Placing MARKET {side} order for {quantity} of {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol, 
                side=side.upper(), 
                type='MARKET', 
                quantity=quantity
            )
            logging.info("API Response: %s", order)
            print("--- ✅ Market Order Successful ---")
            print(f"Details: {order}")
            return order
        except BinanceAPIException as e:
            logging.error("API Error placing market order: %s", e)
            print(f"--- ❌ Error: {e.message} ---")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        """Places a limit order."""
        try:
            logging.info(f"Placing LIMIT {side} order for {quantity} of {symbol} at {price}")
            order = self.client.futures_create_order(
                symbol=symbol, 
                side=side.upper(), 
                type='LIMIT', 
                quantity=quantity, 
                price=price, 
                timeInForce='GTC'
            )
            logging.info("API Response: %s", order)
            print("--- ✅ Limit Order Successful ---")
            print(f"Details: {order}")
            return order
        except BinanceAPIException as e:
            logging.error("API Error placing limit order: %s", e)
            print(f"--- ❌ Error: {e.message} ---")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """Places a stop-limit order."""
        try:
            logging.info(f"Placing STOP_LIMIT {side} order for {quantity} of {symbol} at {price} with stop {stop_price}")
            order = self.client.futures_create_order(
                symbol=symbol, 
                side=side.upper(), 
                type='STOP_MARKET', 
                quantity=quantity, 
                stopPrice=stop_price,
                timeInForce='GTC'
            )
            logging.info("API Response: %s", order)
            print("--- ✅ Stop-Limit Order Successful ---")
            print(f"Details: {order}")
            return order
        except BinanceAPIException as e:
            logging.error("API Error placing stop-limit order: %s", e)
            print(f"--- ❌ Error: {e.message} ---")
            return None