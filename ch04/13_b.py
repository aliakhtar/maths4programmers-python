from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *


# Min proj 4.3
# What happens when you scale it by a factor of -1?

f = scale_by(-1)

draw_model(polygon_map(f, load_triangles()))
