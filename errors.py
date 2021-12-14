def absolute_error(error_value, value):
    return abs(error_value - value)


def relative_error(error_value, value):
    if value == 0:
        return 'condition: x != 0'
    return abs((error_value - value) / value)


def max_absolute_error(base, exponent, mantissa_positions):
    if base % 2 != 0:
        return 'condition: base needs to be even'
    return (base / 2) * base ** (exponent - mantissa_positions - 1)


# example: x = 0.1801234567 * 10^3, round to 7 mantissas
# => |rd(x)-x| <= 5 * 10^(-5)
base = 10
exponent = 3
mantissa_positions = 7
print(max_absolute_error(base, exponent, mantissa_positions))


def get_eps(base, mantissa_positions):
    """ Maschinengenauigkeit: max relative error on rd(x)
    Kleinste positive Maschinenzahl, für die auf dem Rechner 1 + eps != 1 gilt
    """
    return (base / 2) * base ** (-mantissa_positions)


def max_absolute_func_error(function, error_value, value):
    return abs(function(error_value) - function(value))


# example: x_tilde: 2.0001, x: 2, func: x^2 => max abs. error: 0.0004...
function = lambda x: x ** 2
error_value = 2.0001
value = 2
print(max_absolute_func_error(function, error_value, value))


def max_relative_func_error(function, error_value, value):
    return abs((function(error_value) - function(value)) / function(value))


def condition_number(function, derivative, value):
    return abs(derivative(value)) * abs(value) / abs(function(value))


# example: func: x^2, deriv: 2x, x: 2 => konditioinszahl: 2
function = lambda x: x ** 2
derivative = lambda x: 2 * x
value = 2
print(condition_number(function, derivative, value))


def approximative_max_relative_func_error_using_cond(
        function, derivative, error_value, value):
    return (
        condition_number(function, derivative, value) *
        relative_error(error_value, value)
    )


# example: func: x^2, deriv: 2x, x:2, x_tilde: 2.0001
# => approx max rel error: 2
function = lambda x: x ** 2
derivative = lambda x: 2 * x
error_value = 2.0001
value = 2
print(condition_number(function, derivative, value))
