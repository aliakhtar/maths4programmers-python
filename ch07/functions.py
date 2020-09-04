import numpy as np
from ch07.vectors import distance


def standard_form(v1, v2):
    x1, y1 = v1
    x2, y2 = v2

    a = y2 - y1
    b = x1 - x2
    c = (x1 * y2) - (x2 * y1)

    return a, b, c


def intersection(u1, u2, v1, v2):
    a1, b1, c1 = standard_form(u1, u2)
    a2, b2, c2 = standard_form(v1, v2)
    matrix = np.array(((a1, b1), (a2, b2)))
    output = np.array((c1, c2))
    return np.linalg.solve(matrix, output)


def do_segments_intersect(s1, s2):
    u1, u2 = s1
    v1, v2 = s2
    length1 = distance(*s1)
    length2 = distance(*s2)
    try:
        i = intersection(u1, u2, v1, v2)
        return (
                distance(u1, i) <= length1 and
                distance(u2, i) <= length1 and
                distance(v1, i) <= length2 and
                distance(v2, i) <= length2
        )
    except np.linalg.linalg.LinAlgError:
        return False


def standard_form_3d(p1, p2, p3):
    from ch07.vectors import subtract, cross, dot
    parallel1 = subtract(p2, p1)
    parallel2 = subtract(p3, p1)
    a, b, c = cross(parallel1, parallel2)
    d = dot((a, b, c), p1)
    return (a, b, c, d)
