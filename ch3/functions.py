from math import sqrt


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