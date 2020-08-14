from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *


# Min proj 4.3
# What happens to the teapot when you scale every vector by a scalar between 0 and 1?

f = scale_by(0.5)

draw_model(polygon_map(f, load_triangles()))
