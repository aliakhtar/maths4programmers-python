from ch06.Vec2 import Vec2


# Represents a function of the form f(x) = ax + b where a and b are scalars / constants
class LinearFunction2(Vec2):

    def __call__(self, x):
        return (self.x * x) + self.y

    @classmethod
    def zero(cls):
        return LinearFunction2(0, 0)