def average(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
