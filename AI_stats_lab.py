import numpy as np


# -------------------------------------------------
# Question 1: Continuous pair on the unit square
# -------------------------------------------------

def joint_cdf_unit_square(x, y):
    """
    Return the joint CDF F_XY(x, y) for (X, Y) uniform on the unit square.
    """
    if x <= 0 or y <= 0:
        return 0.0
    elif 0 < x < 1 and 0 < y < 1:
        return float(x * y)
    elif 0 < x < 1 and y >= 1:
        return float(x)
    elif x >= 1 and 0 < y < 1:
        return float(y)
    else:  # x >= 1 and y >= 1
        return 1.0


def rectangle_probability(x1, x2, y1, y2):
    """
    Compute P(x1 < X <= x2, y1 < Y <= y2)
    using the joint CDF rectangle formula:
    P = F(x2, y2) - F(x1, y2) - F(x2, y1) + F(x1, y1)
    """
    term1 = joint_cdf_unit_square(x2, y2)
    term2 = joint_cdf_unit_square(x1, y2)
    term3 = joint_cdf_unit_square(x2, y1)
    term4 = joint_cdf_unit_square(x1, y1)
    return term1 - term2 - term3 + term4


def marginal_fx_unit_square(x):
    """
    Return the marginal PDF f_X(x) for X when (X, Y) is uniform on the unit square.
    """
    if 0 < x < 1:
        return 1.0
    return 0.0


def marginal_fy_unit_square(y):
    """
    Return the marginal PDF f_Y(y) for Y when (X, Y) is uniform on the unit square.
    """
    if 0 < y < 1:
        return 1.0
    return 0.0


# -------------------------------------------------
# Question 2: Joint PMF, marginals, independence
# -------------------------------------------------

def joint_pmf_heads(x, y):
    """
    Return P_XY(x, y) for:
    X = number of heads in the first toss (0 or 1)
    Y = total number of heads in both tosses (0, 1, or 2)
    """
    pmf_table = {
        (0, 0): 1/4, (0, 1): 1/4, (0, 2): 0,
        (1, 0): 0,   (1, 1): 1/4, (1, 2): 1/4
    }
    return pmf_table.get((x, y), 0)


def marginal_px_heads(x):
    """
    Return P_X(x) by summing the joint PMF over y (0, 1, 2).
    """
    return sum(joint_pmf_heads(x, y) for y in [0, 1, 2])


def marginal_py_heads(y):
    """
    Return P_Y(y) by summing the joint PMF over x (0, 1).
    """
    return sum(joint_pmf_heads(x, y) for x in [0, 1])


def check_independence_heads():
    """
    Return True if X and Y are independent, else False.
    Check if P(X=x, Y=y) = P(X=x) * P(Y=y) for all x, y.
    """
    for x in [0, 1]:
        for y in [0, 1, 2]:
            joint = joint_pmf_heads(x, y)
            marginal_prod = marginal_px_heads(x) * marginal_py_heads(y)
            # Use np.isclose for float comparison safety
            if not np.isclose(joint, marginal_prod):
                return False
    return True
