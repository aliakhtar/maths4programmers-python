from math import *
from random import *


def add(*vectors):
    coordTuples = zip(*vectors)
    coordSums = [ sum(coords) for coords in coordTuples ]
    return tuple(coordSums)


def length(vector):
    squares = [coord ** 2 for coord in vector]
    squareSums = sum(squares)
    return sqrt(squareSums)


def scale(s, v):
    scaled = tuple(x * s for x in v)
    return scaled


def dot(u, v):
    coords = zip(u, v)
    coordProds = [x * y for x, y in coords]
    return sum(coordProds)

def angle_between(u, v):
    # cos(angle) = dotProduct / product of lengths
    # angle = acos(dotProd / product of lengths)
    dotProd = dot(u, v)
    lengthProd = length(u) * length(v)
    angle = acos( dotProd / lengthProd )
    return angle


def rand_angle():
    deg = randint(1, 361)
    #return deg
    return deg * pi / 180


# noinspection PyRedundantParentheses
def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)