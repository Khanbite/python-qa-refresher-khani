def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Not enough money.")
    return balance - amount
