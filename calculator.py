# https://github.com/dylanduley/lab11-DD-TJ
# Partner 1: Dylan Duley
# Partner 2: Ty Jackson

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError

    return math.log(b, a)

def exponent(a, b):
    return a ** b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError

    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError

    return math.log(b, a)

def exp(a, b):
    return a ** b
