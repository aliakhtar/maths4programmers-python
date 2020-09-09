import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import ch11.vectors as vectors


def gravitational_field(source, x, y):
    relative_position = (x - source.x, y - source.y)
    return vectors.scale(-source.gravity, relative_position)


def gravitational_field_sum(sources, x,y):
    return vectors.add(*[gravitational_field(s, x, y) for s in sources])


def plot_vector_field(f,xmin,xmax,ymin,ymax,xstep=1,ystep=1):

    X,Y = np.meshgrid(np.arange(xmin,xmax, xstep),np.arange(ymin,ymax, ystep))
    U = np.vectorize(lambda x,y : f(x,y)[0])(X,Y)
    V = np.vectorize(lambda x,y : f(x,y)[1])(X,Y)
    plt.quiver(X, Y, U, V,color='red')
    fig = plt.gcf()
    fig.set_size_inches(7,7)


def plot_scalar_field(f, xmin, xmax, ymin, ymax, xstep=0.25, ystep=0.25, c=None, cmap=cm.coolwarm, alpha=1,
                      antialiased=False):
    fig = plt.figure()
    fig.set_size_inches(7, 7)
    ax = fig.gca(projection='3d')

    fv = np.vectorize(f)

    # Make data.
    X = np.arange(xmin, xmax, xstep)
    Y = np.arange(ymin, ymax, ystep)
    X, Y = np.meshgrid(X, Y)
    Z = fv(X, Y)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, color=c, alpha=alpha,
                           linewidth=0, antialiased=antialiased)


def scalar_field_heatmap(f, xmin, xmax, ymin, ymax, xstep=0.1, ystep=0.1):
    fig = plt.figure()
    fig.set_size_inches(7, 7)

    fv = np.vectorize(f)

    X = np.arange(xmin, xmax, xstep)
    Y = np.arange(ymin, ymax, ystep)
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
    plt.xlabel('x')
    plt.ylabel('y')


def scalar_field_contour(f, xmin, xmax, ymin, ymax, levels=None):
    fv = np.vectorize(f)

    X = np.arange(xmin, xmax, 0.1)
    Y = np.arange(ymin, ymax, 0.1)
    X, Y = np.meshgrid(X, Y)

    # https://stackoverflow.com/a/54088910/1704140
    Z = fv(X, Y)

    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z, levels=levels)
    ax.clabel(CS, inline=1, fontsize=10, fmt='%1.1f')
    plt.xlabel('x')
    plt.ylabel('y')
    fig.set_size_inches(7, 7)