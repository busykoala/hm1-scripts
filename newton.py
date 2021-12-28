from dataclasses import dataclass
from pprint import pprint as pp
import math


@dataclass
class NewtonIterationRow:
    iteration: int
    x: float
    error: float


def newton_iteration(function, derivative, x0, min_error=0.001, max_iteration=3):
    iter_count = 0
    error = 1
    rows = []
    while error > min_error and iter_count < max_iteration:
        x = x0 - (function(x0) / derivative(x0))
        error = abs(x0 - x)
        x0 = x
        iter_count += 1
        rows.append(NewtonIterationRow(iteration=iter_count, x=x, error=error))
    return rows


# example: func: e^x - x - 2, derivative: e^x - 1, x0: -3
function = lambda x: math.e ** x - x - 2
derivative = lambda x: math.e ** x - 1
x0 = -3
pp(newton_iteration(function, derivative, x0))


def newton_iteration_simplified(function, derivative, x0, min_error=0.001, max_iteration=3):
    x0_const = x0
    iter_count = 0
    error = 1
    rows = []
    while error > min_error and iter_count < max_iteration:
        x = x0 - (function(x0) / derivative(x0_const))
        error = abs(x0 - x)
        x0 = x
        iter_count += 1
        rows.append(NewtonIterationRow(iteration=iter_count, x=x, error=error))
    return rows


# example: func: e^x - x - 2, derivative: e^x - 1, x0: -3
function = lambda x: math.e ** x - x - 2
derivative = lambda x: math.e ** x - 1
x0 = -3
pp(newton_iteration_simplified(function, derivative, x0))
