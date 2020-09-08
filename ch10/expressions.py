from abc import ABC, abstractmethod
import math


def package(item):
    if isinstance(item, int) or isinstance(item, float):
        return Number(item)
    elif isinstance(item, Expression):
        return item
    else:
        raise ValueError("{} could not be packaged, what you doin hoe?".format(item))


def distinct_variables(exp):
    if isinstance(exp, Variable):
        return set(exp.symbol)
    elif isinstance(exp, Number):
        return set()
    elif isinstance(exp, Sum):
        return set().union(*[distinct_variables(exp) for exp in exp.items])
    elif isinstance(exp, Product):
        return distinct_variables(exp.left).union(distinct_variables(exp.right))
    elif isinstance(exp, Power):
        return distinct_variables(exp.base).union(distinct_variables(exp.exponent))
    elif isinstance(exp, Apply):
        return distinct_variables(exp.arg)
    else:
        raise TypeError("Not a valid expression.")


# Exercise 10.9: Write a function contains(expression, variable) that checks whether the given expression
# contains any occurrence of the specified variable.
def contains(expr, var):
    if isinstance(expr, Number):
        return False
    elif isinstance(expr, Variable):
        return expr.symbol == var.symbol
    elif isinstance(expr, Sum):
        return any(contains(i, var) for i in expr.items)
    elif isinstance(expr, Product):
        return contains(expr.left, var) or contains(expr.right, var)
    elif isinstance(expr, Power):
        return contains(expr.base, var) or contains(expr.exponent, var)
    elif isinstance(expr, Apply):
        return contains(expr.arg, var)
    else:
        raise TypeError("Not a valid expression")


class Expression(ABC):
    def __add__(self, other):
        return Sum(self, package(other))

    def __sub__(self, other):
        return Difference(self, package(other))

    def __mul__(self, other):
        return Product(self, package(other))

    def __rmul__(self, other):
        return Product(package(other), self)

    def __call__(self, **bindings):
        return self.evaluate(**bindings)

    @abstractmethod
    def expand(self):
        pass

    @abstractmethod
    def evaluate(self, **bindings):
        pass


class Number(Expression):

    def __init__(self, number):
        self.number = number

    def evaluate(self, **bindings):
        return self.number

    def expand(self):
        return self


class Variable(Expression):
    def __init__(self, symbol):
        self.symbol = symbol

    def evaluate(self, **bindings):
        try:
            return bindings[self.symbol]
        except:
            raise KeyError("{} variable is not bound".format(self.symbol))

    def expand(self):
        return self


class Power(Expression):
    def __init__(self, base, exponent):
        self.exponent = exponent
        self.base = base

    def evaluate(self, **bindings):
        return self.base.evaluate(**bindings) ** self.exponent.evaluate(**bindings)

    def expand(self):
        pass


class Product(Expression):
    def __init__(self, left_e, right_e):
        self.left = left_e
        self.right = right_e

    def evaluate(self, **bindings):
        return self.left.evaluate(**bindings) * self.right.evaluate(**bindings)

    def expand(self):
        leftExpanded = self.left.expand()
        rightExpanded = self.right.expand()
        if isinstance(leftExpanded, Sum):
            return Sum(*[Product(e, rightExpanded).expand() for e in leftExpanded.items])
        elif isinstance(rightExpanded, Sum):
            return Sum(*[Product(e, rightExpanded) for e in leftExpanded.items])
        else:
            return Product(leftExpanded, rightExpanded)


class Quotient(Expression):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self, **bindings):
        return self.numerator.evaluate(**bindings) / self.denominator.evaluate(**bindings)

    def expand(self):
        pass


class Sum(Expression):
    def __init__(self, *items):
        self.items = items

    def evaluate(self, **bindings):
        return sum([i.evaluate(**bindings) for i in self.items])

    def expand(self):
        return Sum(*[e.expand for e in self.items])


class Difference(Expression):
    def __init__(self, bigger, smaller):
        self.bigger = bigger
        self.smaller = smaller

    def evaluate(self, **bindings):
        return self.bigger.evaluate(**bindings) - self.smaller.evaluate(**bindings)

    def expand(self):
        pass


class Negative(Expression):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, **bindings):
        return -1 * self.expression.evaluate(**bindings)

    def expand(self):
        pass


class Function():
    _function_bindings = {
        "sin": math.sin,
        "cos": math.cos,
        "ln": math.log,
        "sqrt": math.sqrt,
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

    def expand(self):
        pass
