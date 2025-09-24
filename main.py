# main.py
import logging
from src import cli

# This is where you can configure the project-wide logging
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    # This calls the run function from your cli.py file
    cli.run()