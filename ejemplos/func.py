import numpy as np
from numpy import sin, cos

def stiffness_armor(E, A, L):
    k = E * A / L * np.array([[1, -1], [-1, 1]])
    #T = np.array([np.cos(alpha), np.sin(alpha)])
    return np.kron(np.array([[1, -1], [-1, 1]]), k)

def stiffness_beam(E, I, L):
    k = E*I * np.array([
        [ 12/L**3,  6/L**2, -12/L**3,  6/L**2],
        [  6/L**2,  4/L   ,  -6/L**2,  2/L   ],
        [-12/L**3, -6/L**2,  12/L**3, -6/L**2],
        [  6/L**2,  2/L   ,  -6/L**2,  4/L   ],
    ])
    return k
    
def stiffness_2d(E, A, I, L):
    k = np.zeros((6,6))
    idx_EA = np.array([
        [[0, 0],[3, 3]],
        [[0, 3],[0, 3]]
    ])
    idx_EI = np.array([
        [[1,1,1,1], [2,2,2,2], [4,4,4,4], [5,5,5,5]],
        [[2,3,5,6], [0,1,4,5], [0,1,4,5], [0,1,4,5]],
    ])

    k[idx_EA] = stiffness_EA(E, A, L)
    k[idx_EI] = stiffness_beam(E, I, L)

    return k

def rot_armor(alpha):
    t = np.array([
        [ cos(alpha), sin(alpha)],
        [-sin(alpha), cos(alpha)]
    ])
    return np.kron(np.eye(2), t)

def rot_2d(alpha):
    t = np.array([
        [ cos(alpha), sin(alpha), 0],
        [-sin(alpha), cos(alpha), 0],
        [          0,          0, 1]
    ])
    return np.kron(np.eye(2), t)

def rot_beam(alpha):
    t = np.array([
        [cos(alpha), 0],
        [0         , 1],
    ])
    return np.kron(np.eye(2), t)



