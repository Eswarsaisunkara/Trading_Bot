from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceTestnetClient:
    def __init__(self):
        self.client = Client(
            os.getenv('API_KEY'), 
            os.getenv('API_SECRET'), 
            testnet=True
        )