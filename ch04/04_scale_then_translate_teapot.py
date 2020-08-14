from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *

s = scale_by(2)
t = translate_by((-1, 0, 0))


moved = polygon_map( compose(t, s), load_triangles() )
draw_model(moved)