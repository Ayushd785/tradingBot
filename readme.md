# 🚀 Binance Futures Trading Bot

A Python command-line trading bot for automated order placement on Binance Futures Testnet. Built with clean architecture, comprehensive error handling, and support for multiple order types including market, limit, and stop-limit orders.

## ✨ Features

- **Market Orders**: Instant buy/sell execution at current market price
- **Limit Orders**: Place orders at specific price levels
- **Stop-Limit Orders**: Advanced orders with trigger conditions _(bonus feature)_
- **CLI Interface**: User-friendly command-line interface with input validation
- **Logging**: Complete API request/response logging for transparency
- **Error Handling**: Robust error management with detailed feedback
- **Testnet Safe**: Uses Binance Testnet for risk-free testing

## 🛠️ Setup

### 1. Get Binance Testnet API Keys

Visit [Binance Testnet](https://testnet.binancefuture.com) and create API credentials.

### 2. Install & Configure

```bash
# Clone and navigate to project
git clone <your-repo-url>
cd tradingBot

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
# Create .env file with your API keys:
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
```

## 🎯 Usage

### Market Orders

Execute immediately at current market price:

```bash
python main.py market BTCUSDT buy 0.001
python main.py market ETHUSDT sell 0.01
```

### Limit Orders

Place orders at specific price levels:

```bash
python main.py limit BTCUSDT buy 0.001 --price 45000
python main.py limit ETHUSDT sell 0.01 --price 3500
```

### Stop-Limit Orders

Advanced orders with trigger conditions:

```bash
python main.py stop-limit BTCUSDT sell 0.001 --price 49000 --stop-price 50000
```

### Help

View all available options:

```bash
python main.py --help
```

## 📊 Monitoring

All trading activity is logged to `trading_bot.log` with timestamps, API requests, responses, and error details for complete transparency and debugging.

---

_Built for Binance Futures Testnet • Safe Testing Environment • No Real Money at Risk_
