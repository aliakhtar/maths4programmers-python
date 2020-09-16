import matplotlib.pyplot as plt
import numpy as np


def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)


def plot_sequence(points, max=100, line=False, **kwargs):
    if line:
        plt.plot(range(0, max), points[0:max], **kwargs)
    else:
        plt.scatter(range(0, max), points[0:max], **kwargs)