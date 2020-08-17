from ch05.teapot import load_triangles
from ch05.draw_model import draw_model
import ch05.camera as camera
from math import sin,cos


def get_rotation_matrix(t):
    s = t / 1000
    return (
        (cos(s), 0, sin(s)),
        (0, 1, 0),
        (sin(s), 0, cos(s))
    )

#camera.default_camera = camera.Camera('fig_5.4_draw_teapot',[0,1000,2000,3000,4000])
draw_model(load_triangles(), get_matrix=get_rotation_matrix)
