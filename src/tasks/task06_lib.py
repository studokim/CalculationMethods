import numpy as np
import math
from enum import Enum, auto


def find_max_nondiag(A):
    x, y = 0, 1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if np.abs(A[x][y]) < np.abs(A[i][j]):
                x, y = i, j
    return x, y


def is_in_gershgorin_circle(A, lambda_k):
    circles = []
    for i in range(len(A)):
        sum = 0
        for j in range(len(A)):
            sum += np.abs(A[i][j])
        circles.append([A[i][i], sum - np.abs(A[i][i])])
    for [center, radius] in circles:
        if np.abs(center - lambda_k) <= radius:
            return True
    return False


class Strategy(Enum):
    MAX_ELEMENT = auto()
    CYCLE_CHOICE = auto()


# только для эрмитовых, т.е. (здесь) самосопряжённых
def solve(A, epsilon, strategy):
    x, y = 0, 0
    iter = 0
    cur_A = A.copy()
    size = len(cur_A)

    while True:
        H = np.array(np.diag(np.full(size, 1, float)))
        if strategy == Strategy.MAX_ELEMENT:
            x, y = find_max_nondiag(cur_A)
        elif strategy == Strategy.CYCLE_CHOICE:
            if (y < size - 1) and (y + 1 != x):
                y += 1
            elif y == size - 1:
                x, y = x + 1, 0
            else:
                y += 2
        if np.abs(cur_A[x][y]) < epsilon:
            return cur_A.diagonal(), iter
        iter += 1
        phi = math.atan(2 * cur_A[x][y] /
                        (cur_A[x][x] - cur_A[y][y])) / 2
        value = math.cos(phi)
        H[y, y] = H[x, x] = value
        H[y, x] = math.sin(phi)
        H[x, y] = -H[y, x]
        cur_A = np.dot(H.T, np.dot(cur_A, H))


def calc_diff(lhs_sorted, rhs):
    return np.linalg.norm(lhs_sorted - sorted(rhs, key=lambda l: abs(l)))
