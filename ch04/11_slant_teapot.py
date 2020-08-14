from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *


def slant_xy(v):
    x, y, z = v
    return (x + y, y, z)


draw_model(polygon_map(slant_xy, load_triangles()))
