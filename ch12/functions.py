import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from math import sin, cos, pi, sqrt
import ch12.vectors as vectors


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


def landing_position(traj):
    return traj[1][-1]


def hang_time(traj):
    # for t, z in (traj[0], traj[2]):
    #    if z <= 0:
    #        return t

    return traj[0][-1]


def max_height(traj):
    return max(traj[2])


def plot_trajectory_metric(metric_f, angles, **settings):
    metrics = [metric_f(trajectory(a, **settings)) for a in angles]
    plt.scatter(angles, metrics)


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


def secant_slope(f, xmin, xmax):
    return (f(xmax) - f(xmin)) / (xmax - xmin)


def approx_derivative(f, x, dx=1e-6):
    return secant_slope(f, x - dx, x + dx)


def approx_gradient(f, x0, y0, dx=1e-6):
    partial_x = approx_derivative(lambda x: f(x, y0), x0, dx=dx)
    partial_y = approx_derivative(lambda y: f(x0, y), y0, dx=dx)
    return (partial_x, partial_y)


B = 0.001
C = 0.005
v = 20
g = -9.81


def velocity_components(v, theta, phi):  # <2>
    vx = v * cos(theta * pi / 180) * cos(phi * pi / 180)
    vy = v * cos(theta * pi / 180) * sin(phi * pi / 180)
    vz = v * sin(theta * pi / 180)
    return vx, vy, vz


def landing_distance(theta, phi):  # <3>
    vx, vy, vz = velocity_components(v, theta, phi)
    v_xy = sqrt(vx ** 2 + vy ** 2)  # <4>
    a = (g / 2) - B * vx ** 2 + C * vy ** 2  # <5>
    b = vz
    landing_time = -b / a  # <6>
    l_distance = v_xy * landing_time  # <7>
    return l_distance


def gradient_ascent(f, x_start, y_start, tolerance=1e-6):
    x, y = x_start, y_start
    grad = approx_gradient(f, x, y)
    while vectors.length(grad) > tolerance:
        x += grad[0]
        y += grad[1]
        grad = approx_gradient(f, x, y)

    return x, y

def gradient_ascent_points(f, x_start, y_start, tolerance=1e-6):
    x, y = x_start, y_start
    grad = approx_gradient(f, x, y)
    xs = [x]
    ys = [y]
    while vectors.length(grad) > tolerance:
        x += grad[0]
        y += grad[1]
        xs.append(x)
        ys.append(y)
        grad = approx_gradient(f, x, y)

    return xs, ys


def scalar_field_heatmap(f, xmin, xmax, ymin, ymax, xsteps=100, ysteps=100):
    fig = plt.figure()
    fig.set_size_inches(7, 7)

    fv = np.vectorize(f)

    X = np.linspace(xmin, xmax, xsteps)
    Y = np.linspace(ymin, ymax, ysteps)
    X, Y = np.meshgrid(X, Y)

    # https://stackoverflow.com/a/54088910/1704140
    z = fv(X, Y)

    #     # x and y are bounds, so z should be the value *inside* those bounds.
    #     # Therefore, remove the last value from the z array.
    #     z = z[:-1, :-1]
    #     z_min, z_max = -z.min(), z.max()

    fig, ax = plt.subplots()

    c = ax.pcolormesh(X, Y, z, cmap='plasma')
    # set the limits of the plot to the limits of the data
    ax.axis([X.min(), X.max(), Y.min(), Y.max()])
    fig.colorbar(c, ax=ax)