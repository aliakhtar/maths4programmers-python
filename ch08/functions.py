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


# Exercise 8.3: Write a function that uses the code from the previous exercise to plot a secant line of a function f
# between two given points.

def plot_secant(f, t1, t2, color='k'):
    line_f = secant_line(f, t1, t2)
    plot_function(line_f, t1, t2, c=color)
    plt.scatter([t1, t2], [f(t1), f(t2)], c=color)


def interval_flow_rates(vol, t1, t2, interval):
    intervals = np.arange(t1, t2, interval)
    return [(t, avg_flow_rate(vol, t, t + interval)) for t in intervals]


def plot_interval_flow_rates(vol, t1, t2, interval):
    series = interval_flow_rates(vol, t1, t2, interval)
    times = [t for (t, _) in series]
    values = [y for (_, y) in series]
    plt.scatter(times, values)


def decreasing_volume(t):
    if t < 5:
        return 10 - (t ** 2) / 5
    else:
        return 0.2 * (10 - t) ** 2


# Exercise 8.5: Write a linear_volume_function and plot the flow rate over time to show that it is constant.
def linear_volume(t):
    return 3 * t + 1


def instantaneous_flow(vol, t, digits=6):
    tolerance = 10 ** (-digits)
    interval = 1
    last_avg_rate = avg_flow_rate(vol, t - interval, t + interval)

    for i in range(0, 2 ** digits):
        interval = interval / 10
        current_avg = avg_flow_rate(vol, t - interval, t + interval)
        difference = abs(last_avg_rate - current_avg)
        if (difference < tolerance):
            return round(current_avg, digits)
        else:
            last_avg_rate = current_avg

    raise Exception("No derivative found")


def get_flow_rate_function(vol):
    return lambda t: instantaneous_flow(vol, t)


def small_volume_change(flow_rate_func, time, duration):
    rate_at_time = flow_rate_func(time)
    volume_change_in_time = rate_at_time * duration
    return volume_change_in_time


def volume_change(flow_rate_func, start, end, interval):
    times = np.arange(start, end, interval)
    return sum([small_volume_change(flow_rate_func, t, interval) for t in times])


def approx_volume(flow_rate_f, initial_vol, interval, t):
    return initial_vol + volume_change(flow_rate_f, 0, t, interval)
