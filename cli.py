import questionary
from validators import validate_order
from orders import place_order
from logging_config import setup_logging

logger = setup_logging()

def main():
    print("--- Binance Futures Testnet Bot ---")
    
    symbol = questionary.text("Enter Symbol (e.g., BTCUSDT):").ask()
    side = questionary.select("Select Side:", choices=["BUY", "SELL"]).ask()
    order_type = questionary.select("Select Order Type:", choices=["MARKET", "LIMIT"]).ask()
    quantity = float(questionary.text("Enter Quantity:").ask())
    
    price = None
    if order_type == "LIMIT":
        price = float(questionary.text("Enter Limit Price:").ask())

    try:
        # Validate inputs
        s, t = validate_order(side, order_type, price)
        
        # Execute order
        print("\nPlacing order...")
        result = place_order(symbol, s, t, quantity, price)
        
        # Display output
        print(f"\n✅ Order Success!")
        print(f"ID: {result['orderId']}")
        print(f"Status: {result['status']}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == '__main__':
    main()