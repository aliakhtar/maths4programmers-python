class Number():
    def __init__(self, n):
        self.number = n


class Variable():
    def __init__(self, symbol):
        self.symbol = symbol


class Power():
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent


class Product():
    def __init__(self, exp1, exp2):
        self.e1 = exp1
        self.e2 = exp2


class Sum():
    def __init__(self, *exps):
        self.exps = exps


class Function():
    def __init__(self, name):
        self.name = name


class Apply():
    def __init__(self, function, argument):
        self.f = function
        self.arg = argument


class Quotient():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


class Difference():
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2
