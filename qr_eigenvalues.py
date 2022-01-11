import numpy as np

from qr_decomposition import qr_decomposition


def qr_eigvals(A, tol=1e-12, maxiter=1000):
    A_old = np.copy(A)
    A_new = np.copy(A)
    diff = np.inf
    i = 0
    while (diff > tol) and (i < maxiter):
        A_old[:, :] = A_new
        Q, R = qr_decomposition(A_old)
        A_new[:, :] = R @ Q
        diff = np.abs(A_new - A_old).max()
        i += 1
    eigvals = np.diag(A_new)
    return eigvals


# example: A here is a random 3x3 matrix
# ! this script needs the qr_decomposition script
A = np.random.random((3, 3))
print(f"--- Matrix A:\n{A}")

eigenvalues = sorted(qr_eigvals(A))
print(f"--- Eigenvalues A:\n{eigenvalues}")

eigenvalues_np = sorted(np.linalg.eigvals(A))
print(f"--- Eigenvalues from numpy A:\n{eigenvalues_np}")
