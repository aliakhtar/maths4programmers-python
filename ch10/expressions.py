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


# Exercise 10.10: Write a distinct_functions function that takes an expression as an argument and returns the
# distinct, named functions (like sin or ln) that appear in the expression.
def distinct_functions(e):
    if isinstance(e, Number) or isinstance(e, Variable):
        return set()
    elif isinstance(e, Sum):
        return set().union(*[distinct_functions(x) for x in e.items])
    elif isinstance(e, Product):
        return distinct_functions(e.left).union(distinct_functions(e.right))
    elif isinstance(e, Power):
        return distinct_functions(e.base).union(distinct_functions(e.exponent))
    elif isinstance(e, Apply):
        return {e.function.name}.union(distinct_functions(e.arg))
    else:
        raise TypeError("Not a valid expression")


# Exercise 10.11: Write a function contains_sum that takes an expression and returns True if it contains a Sum, and
# False otherwise.
def contains_sum(e):
    if isinstance(e, Variable) or isinstance(e, Number):
        return False
    elif isinstance(e, Sum):
        return True
    elif isinstance(e, Product):
        return contains_sum(e.left) or contains_sum(e.right)
    elif isinstance(e, Power):
        return contains_sum(e.base) or contains_sum(e.base)
    elif isinstance(e, Apply):
        return contains_sum(e.arg)
    else:
        raise TypeError("Not a valid expression")


def paren_if_instance(exp, *args):
    for typ in args:
        if isinstance(exp, typ):
            return "\\left( {} \\right)".format(exp.latex())
    return exp.latex()


def dot_if_necessary(latex):
    if latex[0] in '-1234567890':
        return '\\cdot {}'.format(latex)
    else:
        return latex


class Expression(ABC):
    def __add__(self, other):
        return Sum(self, package(other))

    def __sub__(self, other):
        return Difference(self, package(other))

    def __mul__(self, other):
        return Product(self, package(other))

    def __rmul__(self, other):
        return Product(package(other), self)

    def __truediv__(self, other):
        return Quotient(self, package(other))

    def __pow__(self, other):
        return Power(self, package(other))

    def __call__(self, **bindings):
        return self.evaluate(**bindings)

    @abstractmethod
    def expand(self):
        pass

    @abstractmethod
    def simplify(self):
        pass

    @abstractmethod
    def evaluate(self, **bindings):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def latex(self):
        pass

    @abstractmethod
    def derivative(self, var):
        pass

    @abstractmethod
    def substitute(self, var, expression):
        pass

    def __repr__(self):
        return self.display()

    def _repr_latex_(self):
        return "$$" + self.latex() + "$$"


class Number(Expression):

    def __init__(self, number):
        self.number = number

    def evaluate(self, **bindings):
        return self.number

    def expand(self):
        return self

    def simplify(self):
        return self

    def latex(self):
        return str(self.number)

    def display(self):
        return "Number({})".format(self.number)

    def derivative(self, var):
        return Number(0)

    def substitute(self, var, expression):
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

    def simplify(self):
        return self

    def latex(self):
        return self.symbol

    def display(self):
        return "Variable(\"{}\")".format(self.symbol)

    def derivative(self, var):
        if self.symbol == var.symbol:
            return Number(1)
        else:
            return Number(0)

    def substitute(self, var, expression):
        if self.symbol == var.symbol:
            return expression
        else:
            return self


class Power(Expression):
    def __init__(self, base, exponent):
        self.exponent = exponent
        self.base = base

    def evaluate(self, **bindings):
        return self.base.evaluate(**bindings) ** self.exponent.evaluate(**bindings)

    def expand(self):
        return self

    def simplify(self):
        return self

    def latex(self):
        return "{} ^ {{ {} }}".format(
            paren_if_instance(self.base, Sum, Negative, Difference, Quotient, Product),
            self.exponent.latex())

    def substitute(self, var, exp):
        return Power(self.base.substitute(var, exp), self.exponent.substitute(var, exp))

    def display(self):
        return "Power({},{})".format(self.base.display(), self.exponent.display())


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

    def simplify(self):
        pass

    def substitute(self, var, exp):
        return Product(self.left.substitute(var, exp), self.right.substitute(var, exp))

    def derivative(self, var):
        a = Product(self.left.derivative(var), self.right)
        b = Product(self.left, self.right.derivative(var))
        return Sum(a, b)

    def latex(self):
        return "{}{}".format(
            paren_if_instance(self.left, Sum, Negative, Difference),
            dot_if_necessary(paren_if_instance(self.right, Sum, Negative, Difference)))

    def display(self):
        return "Product({},{})".format(self.left.display(), self.right.display())


class Quotient(Expression):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self, **bindings):
        return self.numerator.evaluate(**bindings) / self.denominator.evaluate(**bindings)

    def expand(self):
        return self

    def latex(self):
        return "\\frac{{ {} }}{{ {} }}".format(self.numerator.latex(), self.denominator.latex())

    def substitute(self, var, expression):
        return Quotient(
            self.numerator.substitute(var, expression),
            self.denominator.substitute(var, expression)
        )

    def display(self):
        return "Quotient({},{})".format(self.numerator.display(), self.denominator.display())


class Sum(Expression):
    def __init__(self, *items):
        self.items = items

    def evaluate(self, **bindings):
        return sum([i.evaluate(**bindings) for i in self.items])

    def simplify(self):
        pass

    def expand(self):
        return Sum(*[e.expand for e in self.items])

    def latex(self):
        return " + ".join(exp.latex() for exp in self.items)

    def display(self):
        return "Sum({})".format(",".join([e.display() for e in self.items]))

    def substitute(self, var, expression):
        return Sum(*[i.subsitute(var, expression) for i in self.items])

    def derivative(self, var):
        return Sum(*[i.derivative(var) for i in self.items])


class Difference(Expression):
    def __init__(self, bigger, smaller):
        self.bigger = bigger
        self.smaller = smaller

    def evaluate(self, **bindings):
        return self.bigger.evaluate(**bindings) - self.smaller.evaluate(**bindings)

    def expand(self):
        return self

    def simplify(self):
        pass

    def substitute(self, var, expression):
        return Difference(self.bigger.subsitute(var, expression), self.smaller.substitute(var, expression))

    def display(self):
        return "Difference({},{})".format(self.bigger.display(), self.smaller.display())

    def latex(self):
        return "{} - {}".format(
            self.bigger.latex(),
            paren_if_instance(self.smaller, Sum, Difference, Negative))


class Negative(Expression):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, **bindings):
        return -1 * self.expression.evaluate(**bindings)

    def expand(self):
        return self

    def simplify(self):
        pass

    def latex(self):
        return "- {}".format(
            paren_if_instance(self.expression, Sum, Difference, Negative))

    def substitute(self, var, expression):
        return Negative(self.expression.substitute(var, expression))

    def display(self):
        return "Negative({})".format(self.expression.display())


class Function():
    def __init__(self, name, make_latex=None):
        try:
            self.f = _function_bindings[name]
        except:
            raise KeyError("Function not supported: {}".format(name))

        self.make_latex = make_latex
        self.name = name

    def latex(self, arg_latex):
        if self.make_latex:
            return self.make_latex(arg_latex)
        else:
            return " \\operatorname{{ {} }} \\left( {} \\right)".format(self.name, arg_latex)


class Apply(Expression):
    def __init__(self, function, arg):
        self.function = function
        self.arg = arg

    def evaluate(self, **bindings):
        return self.function.f(self.arg.evaluate(**bindings))

    def expand(self):
        return Apply(self.function, self.arg.expand())

    def simplify(self):
        pass

    def latex(self):
        return self.function.latex(self.arg.latex())

    def display(self):
        return "Apply(Function(\"{}\"),{})".format(self.function.name, self.arg.display())

    def substitute(self, var, expression):
        return Apply(self.function, self.arg.substitute(var, expression))

    def derivative(self, var):
        pass


_var = Variable('placeholder variable')

_function_bindings = {
    "sin": math.sin,
    "cos": math.cos,
    "ln": math.log,
    "sqrt": math.sqrt,  # just to make that one stupid exercise in 10.1 pass. no derivative coded
}

_derivative_bindings = {
    "sin": Apply(Function("cos"), _var),
    "cos": Product(Number(-1), Apply(Function("sin"), _var)),
    "ln": Quotient(Number(1), _var),
}
