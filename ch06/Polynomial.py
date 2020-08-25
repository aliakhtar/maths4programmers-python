from ch06.Vector import Vector


# Represents a class which can implement any polynomial function of the type ax**N...bx + c
# I.e takes in a number of coefficients and a value of x and c,
# and carries out the equation of adding up all the coefficients and powers of X upto the degree indicated by the
# number of coefficients. Eg if two coefficients are given, it'll be a quadratic function of the type
# ax**2 + bx + c

# c is a final constant to add to the end of the equation
class Polynomial(Vector):

    def __init__(self, c, *coefficients):
        self.c = c
        self.coeffs = coefficients

    def __call__(self, x):
        to_add = [self.c]
        for i in range(0, len(self.coeffs)):
            power_of_x = x ** i
            to_add.append(power_of_x)
        return sum(to_add)

    def add(self, other):
        c = self.c + other.c
        coeffs = [a + b for a, b in zip(self.coeffs, other.coeffs)]
        return Polynomial(c, coeffs)

    def scale(self, s):
        c = self.c * s
        coeffs = [co * s for co in self.coeffs]
        return Polynomial(c, coeffs)

    @classmethod
    def zero(cls):
        return Polynomial(0, [0])
