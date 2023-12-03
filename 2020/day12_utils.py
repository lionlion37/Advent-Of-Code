import numpy as np


def spin_vector(vector, degree, d):
    """
    Spins a given numpy vector for -degree- degrees in the given direction -d-.
    :param vector: a 2d numpy vector
    :param degree: number of degrees to spin; has to be a multiple of 90
    :param d: direction in which to spin; has to be either 'L' (left) or 'R' (right)
    :return: spun vector
    """
    for _ in range(int(degree / 90)):
        vector = np.array([vector[1] * (1 if d == 'R' else -1), vector[0] * (1 if d == 'L' else -1)])
    return vector
