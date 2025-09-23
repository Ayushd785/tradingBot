# Simple Binance Futures Trading Bot

This is a command-line application for placing market and limit orders on the Binance Futures Testnet, built as an assignment for the Junior Python Developer role.

## Setup

1.  Clone the repository:
    `git clone <your-repo-url>`
2.  Navigate to the project directory:
    `cd trading-bot-project`
3.  Create and activate a virtual environment:
    `python -m venv venv`
    `source venv/bin/activate`
4.  Install the required dependencies:
    `pip install -r requirements.txt`
5.  Create a `.env` file in the root directory and add your API keys:
    ```
    BINANCE_API_KEY="YOUR_KEY"
    BINANCE_API_SECRET="YOUR_SECRET"
    ```

## Usage

The application is run from the command line.

**Place a market order:**
`python main.py market BTCUSDT buy 0.001`

**Place a limit order:**
`python main.py limit BTCUSDT sell 0.001 --price 50000`
