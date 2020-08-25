from ch06.Vector import Vector


# Represents a class which can implement any polynomial function of the type ax**1 + ax**2...ax**n
# I.e takes in a number of coefficients and a value of x and returns the sum of all the powers of x
#  upto the degree indicated by the number of coefficients.
#  Eg if two coefficients are given, it'll be a quadratic function of the type
# ax**2 + bx**1 + c(x**0) = ax**2 + bx + c

class Polynomial(Vector):

    def __init__(self, *coefficients):
        self.coeffs = coefficients

    def __call__(self, x):
        return sum(
            (x ** power) * coeff
            for power, coeff in enumerate(self.coeffs)
        )

    def add(self, other):
        coeffs = [a + b for a, b in zip(self.coeffs, other.coeffs)]
        return Polynomial(coeffs)

    def scale(self, s):
        coeffs = [co * s for co in self.coeffs]
        return Polynomial(coeffs)

    @classmethod
    def zero(cls):
        return Polynomial(0)
