from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *


# Exercise 4.2

t = (0, 0, -20)
f = translate_by( t)

draw_model(polygon_map(f, load_triangles()))
