from src.tasks.task01_lib import calc_cond_v, k_bad_cond, calc_diff
import numpy as np
from numpy.linalg import norm


def build_random_x(n, max_value=1000):
    return np.random.randint(-max_value, max_value, n)


# метод отражений
def build_QR(A, b):
    def U(w_i, i):
        return np.eye(len(A) - i) - 2 * np.dot(w_i.T, w_i.conjugate())

    b_i = b
    A_i = A
    Q = np.eye(len(A))

    for i in range(0, len(A)-1):
        a_i = A_i[i:, i]
        e_i = np.zeros(len(A) - i)
        e_i[0] = 1

        w_i = (a_i - norm(a_i) * e_i)
        w_i = np.array([w_i/norm(w_i)])

        U_i = np.block([[np.eye(i), np.zeros((i, len(A) - i))],
                        [np.zeros((len(A) - i, i)), U(w_i, i)]])
        b_i = np.dot(U_i, b_i)
        A_i = np.dot(U_i, A_i)
        Q = np.dot(Q, U_i)

    R = A_i
    return Q, R, b_i
