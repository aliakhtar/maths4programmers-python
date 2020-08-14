from ch04.teapot import load_triangles
from ch04.draw_model import draw_model
from ch04.functions import *

bigger = polygon_map( scale_by(2), load_triangles() )
draw_model(bigger)