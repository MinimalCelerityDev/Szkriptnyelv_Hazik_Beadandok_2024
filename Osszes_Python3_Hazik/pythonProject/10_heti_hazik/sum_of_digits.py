# sum_of_digits.py

def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n))
