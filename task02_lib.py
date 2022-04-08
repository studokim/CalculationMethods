from task01_lib import compute_cond_v, k_bad_cond, compute_diff
import numpy as np


def build_LU(A: np.array):
    n = len(A)
    Ai_minus_1 = A
    L = np.identity(n)
    for i in range(1, n):
        Mi = np.identity(n)
        for row in range(i, n):
            Mi[row][i-1] = -Ai_minus_1[row][i-1] / Ai_minus_1[i-1][i-1]
        Ai = np.dot(Mi, Ai_minus_1)
        Ai_minus_1 = Ai
        L = np.dot(Mi, L)
    L = np.linalg.inv(L)
    U = Ai_minus_1
    return L, U


def solve(A: np.array, b: np.array):
    n = len(A)
    L, U = build_LU(A)

    # прямая подстановка
    y = [0 for i in range(n)]
    y[0] = b[0]
    for i in range(1, n):
        y[i] = b[i] - sum([L[i][j] * y[j] for j in range(0, i)])

    # обратная подстановка
    x = np.array([0 for i in range(n)])
    x[n-1] = y[n-1] / U[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - sum([U[i][j] * x[j]
                            for j in range(i+1, n)])) / U[i][i]

    return x


def print_diff(X: np.array, X_: np.array, title_1: str = "решение", title_2: str = "решение матпакета"):
    diff = compute_diff(X, X_)
    print(f"X  = {format_vector(X)} — {title_1}")
    print(f"X_ = {format_vector(X_)} — {title_2}")
    print(f"|X  - X_| = {diff}")


def build_random_vector(length: int):
    vector = np.random.rand(length)
    return -10 + vector * 20


def build_regularization(A: np.array, b: np.array, alpha: float, x0: np.array = None):
    n = len(A)
    if x0 is None:
        x0 = np.array([0 for i in range(n)])
    A_ = A + alpha * np.identity(n)
    b_ = b + alpha * x0
    return A_, b_


def format_float(x: float):
    return "{0:16}".format(np.format_float_scientific(x, precision=9).replace('e+00', ''))


def format_vector(vector: np.array):
    return str(list(map(format_float, vector))).replace("'", "").replace(",", "")


def solve_regularizing(A: np.array, b: np.array, x0: np.array = None, verbosity=0):
    best_alpha = None
    best_x = None
    if x0 is None:
        # предполагаем, что точное решение — [1, 1, ... 1]
        x0 = np.array([1 for i in range(len(A))])

    for i in range(-12, 0):
        alpha = 10**i
        A_, b_ = build_regularization(A, b, alpha, x0)
        x_ = np.dot(np.linalg.inv(A_), b_)
        cond = compute_cond_v(A_)
        error = compute_norm(A, b, x_, alpha)
        if verbosity >= 2:
            print("При alpha={0}: cond={1:16}, погрешность={2:16}"
                  .format(*map(format_float, [alpha, cond, error])))
        if ((cond < k_bad_cond and best_alpha is None)
                or (cond >= k_bad_cond and i == -1)):
            best_alpha = alpha
            best_x = x_
    if verbosity >= 1:
        print(f"best_alpha={best_alpha}")
    return best_x


def compute_norm(A: np.array, b: np.array, x: np.array, alpha: float):
    return np.linalg.norm(A * x - b)**2 + alpha * np.linalg.norm(x)**2
