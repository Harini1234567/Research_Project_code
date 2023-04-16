import numpy as np
import math


def quaternion_to_rotation_matrix(x, y, z, w):
    """ This function takes four arguments x, y, z, and w (quaternion coordinates) and returns a 3x3
    rotation matrix. The function first initialises a 3x3 zero matrix and populates its elements using the input
    quaternion values. The values in the resulting matrix are capped between -1 and 1 using numpy clip function
    before being returned. """

    rot_matrix = np.zeros((3, 3))

    rot_matrix[0, 0] = 1 - 2 * y * y - 2 * z * z
    rot_matrix[0, 1] = 2 * x * y - 2 * w * z
    rot_matrix[0, 2] = 2 * x * z + 2 * w * y
    rot_matrix[1, 0] = 2 * x * y + 2 * w * z
    rot_matrix[1, 1] = 1 - 2 * x * x - 2 * z * z
    rot_matrix[1, 2] = 2 * y * z - 2 * w * x
    rot_matrix[2, 0] = 2 * x * z - 2 * w * y
    rot_matrix[2, 1] = 2 * y * z + 2 * w * x
    rot_matrix[2, 2] = 1 - 2 * x * x - 2 * y * y
    np.clip(rot_matrix, -1, 1, out=rot_matrix)

    return rot_matrix


def get_rotation_angle(rot_matrix):
    """This function takes a 3x3 rotation matrix as an argument and returns the rotation
    angle in radians. The value of the angle is capped between -1 and 1 using numpy clip function
    before being returned. If the angle is NaN, the function returns 0 instead. """
    trace = rot_matrix[0, 0] + rot_matrix[1, 1] + rot_matrix[2, 2]

    theta = np.arccos(np.clip((trace - 1) / 2, -1, 1))

    return theta if not math.isnan(theta) else 0


