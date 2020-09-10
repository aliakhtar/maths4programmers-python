import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from math import sin, cos, pi


def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)


def trajectory(angle, speed=20, dt=0.1, height=0, g=-9.81):
    vx = speed * cos(angle * pi / 180)
    vz = speed * sin(angle * pi / 180)
    t, x, z = 0, 0, height
    times, xs, zs = [t], [x], [z]
    while z > 0:
        vz += dt * g
        x += vx * dt
        z += vz * dt
        t += dt
        times.append(t)
        xs.append(x)
        zs.append(z)

    return times, xs, zs
