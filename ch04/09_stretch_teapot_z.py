from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *


def stretch_z(v):
    x, y, z = v
    return (x, y, z * 4)


draw_model(polygon_map(stretch_z, load_triangles()))
