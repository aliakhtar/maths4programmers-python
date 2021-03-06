from random import uniform, randint
from math import isclose
import numpy as np
import matplotlib.pyplot as plt
from math import sin

from ch06.ImageVector import ImageVector
from ch06.Vec2 import *
from ch06.Vec3 import *
from ch06.Function import *
from ch06.matrices import matrix_multiply


def rand_scalar():
    return uniform(-10, 10)


def rand_vec2():
    return Vec2(rand_scalar(), rand_scalar())


def rand_vec3():
    return Vec3(rand_scalar(), rand_scalar(), rand_scalar())


def rand_function():
    scaler = uniform(-10, 10)
    return Function(lambda x: x * scaler)


def rand_matrix(rows, cols, factory):
    m = tuple(
        tuple(rand_scalar() for _ in range(cols))
        for _ in range(rows)
    )

    return factory(m)


def rand_img():
    rand_pixel = lambda: randint(0, 255)
    from ch06.ImageVector import ImageVector

    pixels = [(rand_pixel(), rand_pixel(), rand_pixel()) for _ in range(500 * 500)]
    return ImageVector(pixels)


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


def approx_equal_matrix(m1, m2):
    if not m1.rows() == m2.rows() or not m1.cols() == m2.cols():
        return False

    for r in range(m1.rows()):
        for c in range(m1.cols()):
            if not isclose(m1.matrix[r][c], m2.matrix[r][c]):
                return False

    return True


def approx_equal_img(i1, i2):
    results = [isclose(c1, c2) for p1, p2 in zip(i1.pixels, i2.pixels)
               for c1, c2 in zip(p1, p2)]

    return all(results)


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


def multiply_vec3_matrix(vec, m):
    vec_m = ((vec.x,), (vec.y,), (vec.z,))
    result = matrix_multiply(m.matrix, vec_m)
    return result


def solid_color(r, g, b):
    total_pixels = ImageVector.size[0] * ImageVector.size[1]
    pixels = [(r, g, b) for _ in range(total_pixels)]
    return ImageVector(pixels)


# Takes a 50x50 matrix of brightness values and returns a 500x500 ImageVector where each pixel's RGB values are set
# to the same as that of the brightness pixel corresponding to that block
def img_from_brightness(brightness_matrix, new_size=ImageVector.size[0] * ImageVector.size[1]):
    def brightness_for_pixel(index):
        # print("{}, {}".format(index, floor(index / 10)))
        max = len(brightness_matrix) - 1
        return brightness_matrix[min(round(index / 10), max)]

    new_pixels = []
    for i in range(new_size):
        brightness_avg = brightness_for_pixel(i)
        new_pixels.append((brightness_avg, brightness_avg, brightness_avg))

    print(str(new_pixels))

    return ImageVector(new_pixels)


def brightness_matrix(img, matrix_size=50 * 50, square_width=10):
    #matrix = [0 for _ in range(matrix_size)]
    matrix = []
    max_index = matrix_size - 1

    def matrix_index(pixel_index):
        return min(pixel_index // 10, max_index)

    square_num = 1
    square_sum = 0
    pixels_in_square = 0
    for index, pixel_coords in enumerate(img.pixels):
        square_boundary = (square_num * square_width * square_width) - 1
        if (index < square_boundary):
            square_sum += sum(pixel_coords) / 3.0
            pixels_in_square += 1
        else: # Square boundary reached;
            square_avg = square_sum / pixels_in_square
            matrix.append(square_avg)
            #print("Sq number: {}, pixels in sq: {}, matrix len: {}".format(square_num, pixels_in_square, len(matrix)))
            square_sum = 0
            pixels_in_square = 0
            square_num += 1
    return matrix