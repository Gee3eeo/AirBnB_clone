#!/usr/bin/python3

def fibonacci(n):
    """Return the nth number in the Fibonacci series."""
    if n < 0:
        raise ValueError("n cannot be negative.")
    elif n in (0, 1):
        return n
    else:
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b
