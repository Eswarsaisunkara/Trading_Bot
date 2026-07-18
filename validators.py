def validate_order(side, order_type, price):
    side = side.upper()
    order_type = order_type.upper()
    
    if side not in ['BUY', 'SELL']:
        raise ValueError("Side must be BUY or SELL")
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Type must be MARKET or LIMIT")
    if order_type == 'LIMIT' and price is None:
        raise ValueError("Price is required for LIMIT orders")
    return side, order_type