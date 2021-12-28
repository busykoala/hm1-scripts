import math
from dataclasses import dataclass
from pprint import pprint as pp


@dataclass
class SecantIterationRow:
    iteration: int
    x0: float
    x1: float
    error: float


def secant_iteration(function, derivative, x0, x1, min_error=0.001, max_iteration=3):
    iter_count = 0
    error = 1
    rows = []
    while error > min_error and iter_count < max_iteration:
        x = x1 - ((x1 - x0) / (function(x1) - function(x0)) * function(x1))
        error = abs(x1 - x)
        x0 = x1
        x1 = x
        iter_count += 1
        rows.append(SecantIterationRow(iteration=iter_count, x0=x0, x1=x1, error=error))
    return rows



# example: func: e^x - x - 2, derivative: e^x - 1, x0: -3, x1: -2
function = lambda x: math.e ** x - x - 2
derivative = lambda x: math.e ** x - 1
x0 = -3
x1 = -2
pp(secant_iteration(function, derivative, x0, x1))
