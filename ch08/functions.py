import matplotlib.pyplot as plt
import numpy as np


def plot_function(f, tmin, tmax, tlabel=None, xlabel=None, axes=False, **kwargs):
    ts = np.linspace(tmin, tmax, 1000)
    if tlabel:
        plt.xlabel(tlabel, fontsize=18)
    if xlabel:
        plt.ylabel(xlabel, fontsize=18)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    if axes:
        total_t = tmax - tmin
        plt.plot([tmin - total_t / 10, tmax + total_t / 10], [0, 0], c='k', linewidth=1)
        plt.xlim(tmin - total_t / 10, tmax + total_t / 10)
        xmin, xmax = plt.ylim()
        plt.plot([0, 0], [xmin, xmax], c='k', linewidth=1)
        plt.ylim(xmin, xmax)


def plot_volume(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)", xlabel="volume (bbl)", axes=axes, **kwargs)


def plot_flow_rate(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)", xlabel="flow rate (bbl/hr)", axes=axes, **kwargs)


def volume(t):
    return (t - 4) ** 3 / 64 + 3.3


def flow_rate(t):
    return 3 * (t - 4) ** 2 / 64


def avg_flow_rate(v, t1, t2):
    deltaVol = v(t2) - v(t1)
    deltaTime = t2 - t1
    return deltaVol / deltaTime


# Exercise 8.2: Write a Python function secant_line(f,x1,x2) that takes a function f(x) and two values, x1 and
# x2, and that returns a new function representing a secant line over time. For instance, if you ran line =
# secant_line(f,x1,x2), then line(3) would give you the y value of the secant line at x = 3 .


def secant_line(f, t1, t2):
    slope = (f(t2) - f(t1)) / (t2 - t1)
    start = f(t1)
    deltaTime = lambda t: t - t1
    return lambda t: start + (deltaTime(t) * slope)
