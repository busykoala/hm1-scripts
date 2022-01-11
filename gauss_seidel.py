import enum

import numpy as np


def is_stop_condition_met(B, x_comp, x_old, tol):
    return ((np.linalg.norm(B, np.inf) / (
        1 - np.linalg.norm(B, np.inf)) * np.linalg.norm((x_comp - x_old),
                                                        np.inf)) < tol)


def jacobi(A, b, x0, tol):
    # left triangular matrix
    L = np.tril(A, -1)
    # inverted diagonal matrix
    D_inverted = np.diag(1 / np.diag(A))
    # right triangular matrix
    R = np.triu(A, 1)
    # iteration matrix
    B = np.matmul(-D_inverted, (L + R))

    x_old = x0
    iterations = 0
    calc = True
    while calc:
        x_comp = np.matmul(B, x_old) + np.matmul(D_inverted, b)
        if is_stop_condition_met(B, x_comp, x_old, tol):
            calc = False
        x_old = x_comp
        iterations = iterations + 1

    apriori = np.ceil((np.log((tol * (1 - np.linalg.norm(B, np.inf))) / (
        np.linalg.norm(
            (np.matmul(np.matmul(-D_inverted, (L + R)), x0) + np.matmul(
                D_inverted, b) - x0), np.inf)))) / np.log(
        np.linalg.norm(B, np.inf)))

    return x_old, iterations, apriori


def seidel(A, b, x0, tol):
    # left triangular matrix
    L = np.tril(A, -1)
    # diagonal matrix
    D = np.diag(np.diag(A))
    # right triangular matrix
    R = np.triu(A, 1)
    # iteration matrix
    B = np.matmul(-np.linalg.inv(D + L), R)

    x_old = x0
    iterations = 0
    calc = True
    while calc:
        x_comp = np.matmul(B, x_old) + np.matmul(np.linalg.inv(D + L), b)
        if is_stop_condition_met(B, x_comp, x_old, tol):
            calc = False
        x_old = x_comp
        iterations = iterations + 1

    apriori = np.ceil((np.log((tol * (1 - np.linalg.norm(B, np.inf))) / (
        np.linalg.norm((np.matmul(np.matmul(-np.linalg.inv(D + L), R),
                                  x_old) + np.matmul(np.linalg.inv(D + L),
                                                     b) - x0),
                       np.inf)))) / np.log(np.linalg.norm(B, np.inf)))
    return x_old, iterations, apriori


class Optimization(enum.Enum):
    JACOBI = (jacobi,)
    SEIDEL = (seidel,)

    def __call__(self, *args, **kwargs):
        return self.value[0](*args, **kwargs)


def jacobi_gauss_seidel(A, b, x0, tol, opt):
    """Optimize by either Jacobi or Gauss-Seidel.
    :param A: Matrix A
    :param b: Vector b
    :param x0: Vector x0 (estimation)
    :param tol: tolerance
    :param opt: optimization
    :return: List of [Iteration-Vector, n-Iterations, a-priori estimated steps]
    """
    return opt(A, b, x0, tol)


A = np.array([[8, 5, 2],
              [5, 9, 1],
              [4, 2, 7]])
b = np.array([[19],
              [5],
              [34]])
x0 = np.array([[1],
               [-1],
               [3]])
tolerance = 1e-4

if __name__ == '__main__':
    print(jacobi_gauss_seidel(A, b, x0, tolerance, Optimization.JACOBI))
    print(jacobi_gauss_seidel(A, b, x0, tolerance, Optimization.SEIDEL))
