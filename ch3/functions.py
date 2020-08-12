def add(*vectors):
    coordTuples = zip(*vectors)
    coordSums = [ sum(coords) for coords in coordTuples ]
    return tuple(coordSums)