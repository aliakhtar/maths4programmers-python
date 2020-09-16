import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, pi


def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)


def plot_sequence(points, max=100, line=False, **kwargs):
    if line:
        plt.plot(range(0, max), points[0:max], **kwargs)
    else:
        plt.scatter(range(0, max), points[0:max], **kwargs)


def make_sinusoid(freq, amp):
    f = lambda t: amp * sin(freq * 2 * pi * t)
    return f


def sample(f, start, end, count):
    mapf = np.vectorize(f)
    ts = np.arange(start, end, (end - start) / count)
    values = mapf(ts)
    return values.astype(np.int16)


def const(n): return 1


def fourier_series(a0, a, b):
    terms = lambda t, f, items: [itemN * f(2 * pi * t * (index + 1))
                                 for (index, itemN) in enumerate(items)]

    def result(t):
        cos_terms = terms(t, cos, a)
        sin_terms = terms(t, sin, b)
        return sum(cos_terms, sin_terms) + (a0*const(t))
    return result
