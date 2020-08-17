from ch05.teapot import load_triangles
from ch05.draw_model import draw_model
import ch05.camera as camera
from ch05.funcions import *
from ch05.vectors import *
from ch05.transforms import *
from math import sin,cos


T = (
        (2,1,1),
        (1,2,1),
        (1,1,2)
)
apply = lambda vec: multiply_matrix_vector(T, vec)

transformed_teapot = polygon_map( apply, load_triangles() )

draw_model(transformed_teapot)