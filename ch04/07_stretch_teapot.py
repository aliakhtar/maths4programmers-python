from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *


def stretch_x(v):
    x,y,z = v
    return (4.0 * x, y, z)


draw_model( polygon_map(stretch_x, load_triangles() ))
