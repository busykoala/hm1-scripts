import sympy as sp

x = sp.Symbol('x')


def derivative(function, x_value=None):
    # get the derivative expression
    if not x_value:
        return sp.diff(function)
    # get the derivatives value at x_value
    return sp.diff(function, x).subs({x: x_value})


# example: differentiate symbolically in the first step
# and then run it for a given x value.
function = sp.log(sp.sqrt(x) + 2)
print(derivative(function))
print(derivative(function, 4))


def integrale(function, left_border=None, right_border=None):
    # indefinite integral
    if not left_border or not right_border:
        return sp.integrate(function)
    # integrate with borders for numerical value
    return sp.integrate(function, (x, left_border, right_border))


# example: integrate for indefinite integral (! x**3/3 means (x**3)/3)
# and then integrate the numerical value using left and right borders
function = x ** 2
print(integrale(function))
print(integrale(function, 1, 10))
