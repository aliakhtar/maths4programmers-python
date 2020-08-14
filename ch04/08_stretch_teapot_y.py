from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *


def stretch_y(v):
    x, y, z = v
    return (x, y * 4, z)


draw_model(polygon_map(stretch_y, load_triangles()))
