from math import sqrt


def add(*vectors):
    coordTuples = zip(*vectors)
    coordSums = [ sum(coords) for coords in coordTuples ]
    return tuple(coordSums)


def length(vector):
    squares = [coord ** 2 for coord in vector]
    squareSums = sum(squares)
    return sqrt(squareSums)