def calculate_discount(price, is_member):
    """
    Returns the discounted price.
    Members receive a 10% discount.
    """
    if price < 0:
        raise ValueError("Price can't be negative.")
    if is_member:
        return price * 0.9
    
    return price
