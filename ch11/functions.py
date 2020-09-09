import numpy as np
import matplotlib.pyplot as plt
import ch11.vectors as vectors

def plot_vector_field(f,xmin,xmax,ymin,ymax,xstep=1,ystep=1):

    X,Y = np.meshgrid(np.arange(xmin,xmax, xstep),np.arange(ymin,ymax, ystep))
    U = np.vectorize(lambda x,y : f(x,y)[0])(X,Y)
    V = np.vectorize(lambda x,y : f(x,y)[1])(X,Y)
    plt.quiver(X, Y, U, V,color='red')
    fig = plt.gcf()
    fig.set_size_inches(7,7)


def gravitational_field(source, x, y):
    relative_position = (x - source.x, y - source.y)
    return vectors.scale(-source.gravity, relative_position)


def gravitational_field_sum(sources, x,y):
    return vectors.add(*[gravitational_field(s, x, y) for s in sources])