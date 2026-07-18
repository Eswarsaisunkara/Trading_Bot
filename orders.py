from client import BinanceTestnetClient
import logging

logger = logging.getLogger("TradingBot")

def place_order(symbol, side, order_type, quantity, price=None):
    client = BinanceTestnetClient().client
    params = {
        'symbol': symbol,
        'side': side,
        'type': order_type,
        'quantity': quantity
    }
    
    if order_type == 'LIMIT':
        params.update({'price': price, 'timeInForce': 'GTC'})

    try:
        logger.info(f"Sending {order_type} order: {params}")
        order = client.futures_create_order(**params)
        logger.info(f"Order Successful: {order['orderId']} - Status: {order['status']}")
        return order
    except Exception as e:
        logger.error(f"Order Failed: {e}")
        raise