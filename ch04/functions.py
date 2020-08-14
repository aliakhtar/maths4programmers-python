from ch04.vectors import *


def polygon_map(transform, polygon_list):
    return [
        [transform(vertex) for vertex in polygon]
        for polygon in polygon_list
    ]


def scale_by(s):
    return lambda v: scale(s, v)


def translate_by(t):
    return lambda v: add(t, v)
