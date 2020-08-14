from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *

moved = polygon_map( translate_by((-1, 0, 0)), load_triangles() )
draw_model(moved)