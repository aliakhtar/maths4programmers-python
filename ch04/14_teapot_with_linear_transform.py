from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *

e1 = (1, 0, 0)
e2 = (0, 1, 0)
e3 = (0, 0, 1)

Ae1 = (1, 1, 1)  # A(e1)
Ae2 = (1, 0, -1)  # A(e2)
Ae3 = (0, 1, 1)  # A(e3)


def apply_a(v):
    # s1, s2, s3 are the scalar values of x, y, z in the vector
    # v can be rewritten as (s1 * e1) + (s2 * e2) + (s3 *e3)
    # By adding these 3 vectors together, we end up with v

    # To apply A to a given vector, we multiply s1, s2, s3 with ae1, ae2, and ae3
    s1, s2, s3 = v
    vectorsToAdd = [
        scale(s1, Ae1),
        scale(s2, Ae2),
        scale(s3, Ae3),
    ]

    return add(*vectorsToAdd)


draw_model(polygon_map(apply_a, load_triangles()))
