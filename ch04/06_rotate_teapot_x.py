from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *
from math import *

draw_model( polygon_map(rotate_x_by(pi / 2), load_triangles() ))
