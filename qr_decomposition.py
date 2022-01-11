import numpy as np
import scipy.linalg


def qr_decomposition(A):
    A = np.copy(A)  # necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')  # change to float
    n = np.shape(A)[0]  # get the shape/size of the matrix A

    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square')

    Q = np.eye(n)
    R = A
    for j in np.arange(0, n - 1):
        a = np.copy(R[j:, j:(j + 1)]).reshape(n - j, 1)  # removes top row and left column
        e = np.eye(n - j)[:, 0].reshape(n - j, 1)  # prepare to fill in values
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = 1
        else:
            sig = -1
        v = a + sig * length_a * e
        u = 1 / np.linalg.norm(v) * v
        H = np.eye(n - j) - 2 * u @ np.transpose(u)  # householder matrix
        Qi = np.eye(n)  # get a A size matrix and ...
        Qi[j:, j:] = H  # ... fill in the values from the householder
        R = Qi @ R  # get the A_n (R) for the next iteration (@ -> matrix multiplication)
        Q = Q @ np.transpose(Qi)

    return Q, R


# example: A is a random 3x3 matrix
A = np.random.random((3, 3))
print(f"--- Matrix A:\n{A}")

Q, R = qr_decomposition(A)
print(f"--- Q matrix (orthogonal part):\n{np.matrix.round(Q, 4)}")
print(f"--- R matrix (right diagonal part):\n{np.matrix.round(R, 4)}")

Q_np, R_np = scipy.linalg.qr(A)
print(f"--- Q matrix from scipy (orthogonal part):\n{np.matrix.round(Q_np, 4)}")
print(f"--- R matrix from scipy (right diagonal part):\n{np.matrix.round(R_np, 4)}")
