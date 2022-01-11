from pprint import pprint as pp

import numpy as np

steps = []


def determinant(M, mul=1):
    width = np.size(M[0])
    if width == 1:
        return mul * M[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(M[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * determinant(m, sign * M[0][i])
        steps.append({"mul": mul, "det-M": M})
    return answer


# If only the value is required use:
# print(np.linalg.det(A))
#
# Otherwise this gets you the steps
# The first step is always the complete matrix followed by a sub matrix and
# its multiplicand. After that it is broken down till the end and the next
# one follows.
A = np.array([[1, 3, 5, 9], [1, 3, 1, 7], [4, 3, 9, 7], [5, 2, 0, 9]])
print(determinant(A))

pp(steps.reverse)
