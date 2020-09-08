from abc import ABC, abstractmethod
import math


def package(item):
    if isinstance(item, int) or isinstance(item, float):
        return Number(item)
    elif isinstance(item, Expression):
        return item
    else:
        raise ValueError("{} could not be packaged, what you doin hoe?".format(item))


def distinct_variables(e):
    if isinstance(e, Number):
        return set()

    elif isinstance(e, Variable):
        return set(e.symbol)

    elif isinstance(e, Product):
        return distinct_variables(e.left).union(distinct_variables(e.right))

    elif isinstance(e, Sum):
        return set().union(*[distinct_variables(e) for e in e.items])

    elif isinstance(e, Difference):
        return distinct_variables(e.bigger).union(distinct_variables(e.smaller))

    elif isinstance(e, Negative):
        return distinct_variables(e.expression)

    elif isinstance(e, Power):
        return distinct_variables(e.base).union(distinct_variables(e.exponent))

    elif isinstance(e, Quotient):
        return distinct_variables(e.numerator).union(distinct_variables(e.denominator))

    elif isinstance(e, Apply):
        return distinct_variables(e.arg)

    else:
        raise TypeError("Not a valid expression: {}".format(e))


class Expression(ABC):
    def __add__(self, other):
        return Sum(self, package(other))

    def __sub__(self, other):
        return Difference(self, package(other))

    def __mul__(self, other):
        return Product(self, package(other))

    def __rmul__(self, other):
        return Product(package(other), self)

    @abstractmethod
    def evaluate(self, **bindings):
        pass


class Number(Expression):

    def __init__(self, number):
        self.number = number

    def evaluate(self, **bindings):
        return self.number


class Variable(Expression):
    def __init__(self, symbol):
        self.symbol = symbol

    def evaluate(self, **bindings):
        try:
            return bindings[self.symbol]
        except:
            raise KeyError("{} variable is not bound".format(self.symbol))


class Power(Expression):
    def __init__(self, base, exponent):
        self.exponent = exponent
        self.base = base

    def evaluate(self, **bindings):
        return self.base.evaluate(**bindings) ** self.exponent.evalute(**bindings)


class Product(Expression):
    def __init__(self, left_e, right_e):
        self.left = left_e
        self.right = right_e

    def evaluate(self, **bindings):
        return self.left.evaluate(**bindings) * self.right.evaluate(**bindings)


class Quotient(Expression):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self, **bindings):
        return self.numerator.evaluate(**bindings) / self.denominator.evaluate(**bindings)


class Sum(Expression):
    def __init__(self, *items):
        self.items = items

    def evaluate(self, **bindings):
        return sum([i.evaluate(**bindings) for i in self.items])


class Difference(Expression):
    def __init__(self, bigger, smaller):
        self.bigger = bigger
        self.smaller = smaller

    def evaluate(self, **bindings):
        return self.bigger.evaluate(**bindings) - self.smaller.evaluate(**bindings)


class Negative(Expression):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, **bindings):
        return -1 * self.expression.evaluate(**bindings)


class Function():
    _function_bindings = {
        "sin": math.sin,
        "cos": math.cos,
        "ln": math.log
    }

    def __init__(self, name):
        try:
            self.f = Function._function_bindings[name]
        except:
            raise KeyError("Function not supported: {}".format(name))

        self.name = name


class Apply(Expression):
    def __init__(self, function, arg):
        self.function = function
        self.arg = arg

    def evaluate(self, **bindings):
        return self.function.f(self.arg.evaluate(**bindings))
