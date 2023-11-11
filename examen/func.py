import numpy as np
from numpy import sin, cos

from itertools import product
import matplotlib.pyplot as plt

def stiffness_armor(E, A, L):
    k = E * A / L * np.array([[1, -1], [-1, 1]])
    return k

def stiffness_beam(E, I, L, c=1):
    k = E*I * np.array([
        [ 12/L**3,  6/L**2, -12/L**3,  6/L**2],
        [  6/L**2,  4/L   ,  -6/L**2,  2/L   ],
        [-12/L**3, -6/L**2,  12/L**3, -6/L**2],
        [  6/L**2,  2/L   ,  -6/L**2,  4/L   ]  
    ])
    # positivo antihorario
    return k
    
def stiffness_2d(E, A, I, L, c=1):
    k = np.zeros((6,6))

    k[*np.meshgrid([0,3], [0,3])] = stiffness_armor(E, A, L)
    k[*np.meshgrid([1,2,4,5], [1,2,4,5])] = stiffness_beam(E, I, L, c)

    return k

def rot_armor(alpha):
    t = np.array([
        [ cos(alpha), sin(alpha)],
        [-sin(alpha), cos(alpha)]
    ])
    kr = np.kron(np.eye(2), t)
    return kr

def rot_2d(alpha):
    t = np.array([
        [ cos(alpha), sin(alpha), 0],
        [-sin(alpha), cos(alpha), 0],
        [          0,          0, 1]
    ])
    kr = np.kron(np.eye(2), t)
    return kr

def rot_armor(alpha):
    t = np.array([
        [ cos(alpha), sin(alpha)],
        [-sin(alpha), cos(alpha) ],
    ])
    kr = np.kron(np.eye(2), t)
    return kr

def rot_beam(alpha):
    t = np.array([
        [cos(alpha), 0],
        [0         , 1],
    ])
    kr = np.kron(np.eye(2), t)
    return kr

def plot_vectors(vectors, ax=None, margin=0.1):
    """
    Plot vectors from a given matrix.

    Parameters:
    - vectors: numpy array of shape (n, 2, 2)
        Matrix representing n vectors, where each vector is defined by its start and end points.
    - ax: matplotlib.axes._subplots.AxesSubplot, optional
        Axes on which to plot the vectors. If not specified, a new figure and axes will be created.

    Returns:
    - ax: matplotlib.axes._subplots.AxesSubplot
        The AxesSubplot object on which the vectors are plotted.
    """
    if ax is None:
        fig, ax = plt.subplots()

    for vector in vectors:
        start_point, end_point = vector[0], vector[1]
        ax.quiver(start_point[0], start_point[1], end_point[0] - start_point[0], end_point[1] - start_point[1], angles='xy', scale_units='xy', scale=1, color='b')

    ax.set_aspect('equal', 'box')
    x_min = vectors[:,:,0].min() - margin
    x_max = vectors[:,:,0].max() + margin
    y_min = vectors[:,:,1].min() - margin
    y_max = vectors[:,:,1].max() + margin
    ax.set_xlim([min(x_min, 0), x_max])
    ax.set_ylim([min(y_min, 0), y_max])
    #ax.set_xlim([min(vectors[:,:,0].min(), 0), max(vectors[:,:,0].max(), 0)])
    #ax.set_ylim([min(vectors[:,:,1].min(), 0), max(vectors[:,:,1].max(), 0)])
    ax.grid(False)
    ax.set_axis_off()
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Vectors Plot')

    return ax
import matplotlib.pyplot as plt

def draw_points(coordinates, ax=None):
    """
    Draw points on a plot and label them with their coordinates.

    Parameters:
    - coordinates: numpy array of shape (n, 2)
        Array representing n points, where each point is defined by its x and y coordinates.
    - ax: matplotlib.axes._subplots.AxesSubplot, optional
        Axes on which to draw the points. If not specified, a new figure and axes will be created.

    Returns:
    - ax: matplotlib.axes._subplots.AxesSubplot
        The AxesSubplot object on which the points are drawn.
    """
    if ax is None:
        fig, ax = plt.subplots()

    for i, (x, y) in enumerate(coordinates):
        ax.scatter(x, y, label=f'Point {i + 1}')
        ax.text(x, y, f'({x}, {y})', fontsize=8, ha='right', va='bottom')

    ax.set_aspect('equal', 'box')
    ax.grid(False)  # Desactivar la cuadrícula
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Points Plot')
    ax.legend()

    return ax