from ch04.vectors import *


def polygon_map(transform, polygon_list):
    return [
        [transform(vertex) for vertex in polygon]
        for polygon in polygon_list
    ]


def compose(f1, f2):
    return lambda x: f1(f2(x))


def scale_by(s):
    return lambda v: scale(s, v)


def translate_by(t):
    return lambda v: add(t, v)


def rotate_2d(angle, v):
    l, a = to_polar(v)
    return to_cartesian((l, a + angle))


def rotate_z(angle, v):
    x, y, z = v
    x2, y2 = rotate_2d(angle, (x, y))
    return x2, y2, z


def rotate_z_by(angle):
    return lambda v: rotate_z(angle, v)


def rotate_x(angle, v):
    x, y, z = v
    y2, z2 = rotate_2d(angle, (y, z))
    return x, y2, z2


def rotate_x_by(angle):
    return  lambda v: rotate_x(angle, v)