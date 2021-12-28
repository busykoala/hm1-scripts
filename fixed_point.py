import math
from dataclasses import dataclass
from pprint import pprint as pp


@dataclass
class FixedPointRow:
    iteration: int
    x: float
    error: float


def fixed_point_iteration(function, x0, min_error=0.001, max_iteration=3):
    iter_count = 0
    error = 1
    rows = []
    while error > min_error and iter_count < max_iteration:
        x = function(x0)
        error = abs(x0 - x)
        x0 = x
        iter_count += 1
        rows.append(FixedPointRow(iteration=iter_count, x=x, error=error))
    return rows


# example: func: sin(x)^(1/3), x0: 0.9
# this example diverges with x0: 1
# ----
# F(x) finden für y(x):
# Vorgehen: y(x) null setzen, dann nach x auflösen
# e.g.: y(x)=x^3-x+0.3 -> F(x):=(x-0.3)^(1/3)
function = lambda x: (math.sin(x)) ** (1/3)
x0 = 0.9
pp(fixed_point_iteration(function, x0, min_error=0.0001, max_iteration=10))


def check_convergence(derivative, x_dash):
    """Get konvergenz (x_dash is the solution already!)

    :param derivative: derivative of fixed point function.
    :param x_dash: solution of x
    :return: info string
    """
    x = derivative(x_dash)
    if x < 1:
        return "konvergiert, anziehend"
    else:
        return "divergiert, abstossend"


# TODO: Banachscher Fixpunktsatz S. 31/32
