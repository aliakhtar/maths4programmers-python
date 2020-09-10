import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from math import sin, cos, pi


def trajectory(angle, speed=20, dt=0.1, height=0, g=-9.81):
    vx = speed * cos(angle * pi / 180)
    vz = speed * sin(angle * pi / 180)
    t, x, z = 0, 0, height
    times, xs, zs = [t], [x], [z]
    while z >= 0:
        vz += dt * g
        x += vx * dt
        z += vz * dt
        t += dt
        times.append(t)
        xs.append(x)
        zs.append(z)

    return times, xs, zs


def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)


def plot_trajectories(*trajs, show_seconds=False):
    for traj in trajs:
        xs, zs = traj[1], traj[2]
        plt.plot(xs, zs)
        if show_seconds:
            second_indices = []
            second = 0
            for i, t in enumerate(traj[0]):
                if t >= second:
                    second_indices.append(i)
                    second += 1
            plt.scatter([xs[i] for i in second_indices], [zs[i] for i in second_indices])
    xl = plt.xlim()
    plt.plot(plt.xlim(), [0, 0], c='k')
    plt.xlim(*xl)

    width = 7
    coords_height = (plt.ylim()[1] - plt.ylim()[0])
    coords_width = (plt.xlim()[1] - plt.xlim()[0])
    plt.gcf().set_size_inches(width, width * coords_height / coords_width)