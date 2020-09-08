class Number():
    def __init__(self, number):
        self.number = number

class Variable():
    def __init__(self, symbol):
        self.symbol = symbol

class Power():
    def __init__(self, base, exponent):
        self.exponent = exponent
        self.base = base

class Product():
    def __init__(self, left_e, right_e):
        self.left = left_e
        self.right = right_e

class Sum():
    def __init__(self, *items):
        self.items = items

class Function():
    def __init__(self, name):
        self.items = name

class Apply():
    def __init__(self, function, arg):
        self.function = function
        self.arg = arg

