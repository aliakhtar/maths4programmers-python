from abc import ABC


def package(item):
    if isinstance(item, int) or isinstance(item, float):
        return Number(item)
    elif isinstance(item, Expression):
        return item
    else:
        raise ValueError("{} could not be packaged, what you doin hoe?".format(item))


class Expression(ABC):
    def __add__(self, other):
        return Sum(self, package(other))

    def __sub__(self, other):
        return Difference(self, package(other))

    def __mul__(self, other):
        return Product(self, package(other))

    def __rmul__(self, other):
        return Product(package(other), self)


class Number(Expression):
    def __init__(self, number):
        self.number = number


class Variable(Expression):
    def __init__(self, symbol):
        self.symbol = symbol


class Power(Expression):
    def __init__(self, base, exponent):
        self.exponent = exponent
        self.base = base


class Product(Expression):
    def __init__(self, left_e, right_e):
        self.left = left_e
        self.right = right_e


class Quotient(Expression):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


class Sum(Expression):
    def __init__(self, *items):
        self.items = items


class Difference(Expression):
    def __init__(self, bigger, smaller):
        self.bigger = bigger
        self.smaller = smaller


class Negative(Expression):
    def __init__(self, expression):
        self.expression = expression


class Function(Expression):
    def __init__(self, name):
        self.items = name


class Apply(Expression):
    def __init__(self, function, arg):
        self.function = function
        self.arg = arg
