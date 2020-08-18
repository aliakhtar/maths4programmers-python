from random import uniform
from math import isclose
from ch06.Vec2 import *
from ch06.Vec3 import *


def rand_scalar():
    return uniform(-10, 10)


def rand_vec2():
    return Vec2(rand_scalar(), rand_scalar())


def approx_equal_vec2(u, v):
    return isclose(u.x, v.x) and isclose(u.y, v.y)


def test(eq, a, b, u, v, w):
    assert eq(u + v, v + u)
    assert eq(u + (v + w), (u + v) + w)
    assert eq(a * (b * v), (a * b) * v)
    assert eq(1 * v, v)
    assert eq((a + b) * v, a * v + b * v)
    assert eq(a * v + a * w, a * (v + w))

