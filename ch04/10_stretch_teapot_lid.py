from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *


def cube_y(v):
    x, y, z = v
    return (x, y * y * y, z)


draw_model(polygon_map(cube_y, load_triangles()))
