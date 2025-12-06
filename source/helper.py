from math import isnan
from numpy import tan, arccos, polyval

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    if isnan(float(n)):
        return False
    return True

# Involute Function
def invF(angle):
    """Computes the involute function of a given profile angle.

    All angles in radians.
    """

    return tan(angle) - angle

# Reverse Involute Function
def revInvF(angle):
    """Computes the reverse involute function, returning the profile angle.

    From "The Geometry of Involute Gears" by J.R. Colbourne
    Eqs. 2.16 - 2.17

    All angles in radians.
    """

    q = angle**(2/3)

    poly = [-0.00048, 0.00319, -0.00894, -0.00321, 0.32451, 1.04004, 1]
    x = polyval(poly, q)

    return arccos(1/x)
