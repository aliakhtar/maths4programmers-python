from random import uniform
from math import isclose
import numpy as np
import matplotlib.pyplot as plt
from math import sin
from ch06.Vec2 import *
from ch06.Vec3 import *


def rand_scalar():
    return uniform(-10, 10)


def rand_vec2():
    return Vec2(rand_scalar(), rand_scalar())


def rand_vec3():
    return Vec3(rand_scalar(), rand_scalar(), rand_scalar())


def approx_equal_vec2(u, v):
    return isclose(u.x, v.x) and isclose(u.y, v.y)


def approx_equal_vec3(u, v):
    return isclose(u.x, v.x) and isclose(u.y, v.y) and isclose(u.z, v.z)


def approx_equal_funcs(f, g):
    for _ in range(10):
        x = uniform(-10, 10)
        if not isclose(f(x), g(x)):
            return False

    return True


def test(eq, a, b, u, v, w):
    assert eq(u + v, v + u)
    assert eq(u + (v + w), (u + v) + w)
    assert eq(a * (b * v), (a * b) * v)
    assert eq(1 * v, v)
    assert eq((a + b) * v, a * v + b * v)
    assert eq(a * v + a * w, a * (v + w))

    for vector in [u, v, w]:
        if not hasattr(vector, "zero"):
            return
        assert eq(vector.zero() + vector, vector)
        assert eq(0 * vector, vector.zero())
        assert eq(-vector + vector, vector.zero())


def test_vectors(generator, eq, iterations=100):
    for _ in range(iterations):
        a, b = rand_scalar(), rand_scalar()
        u, v, w = generator(), generator(), generator()
        # print("{}, {}, {}".format(u, v, w))
        test(eq, a, b, u, v, w)

    print("All tests passed")


# plotting utility function for functions in this chapter
def plot(fs, xmin, xmax):
    xs = np.linspace(xmin, xmax, 100)
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    for f in fs:
        ys = [f(x) for x in xs]
        plt.plot(xs, ys)
