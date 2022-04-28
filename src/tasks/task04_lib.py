from cmath import inf, nan
import numpy as np

from src.tasks.task01_lib import calc_diff


def calc_aposterior(alpha: np.array, x_k: np.array, x_k_minus_1: np.array):
    alpha_norm = np.linalg.norm(alpha)
    error = np.linalg.norm(x_k - x_k_minus_1) * \
        alpha_norm / abs(1 - alpha_norm)
    return error


def build_x_k(alpha: np.array, beta: np.array, x_k_minus_1: np.array):
    a = beta + np.dot(alpha, x_k_minus_1)
    return a


def build_alpha(A: np.array):
    n = len(A)
    alpha = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                alpha[i][j] = -A[i][j] / A[i][i]
    return np.array(alpha)


def build_beta(A: np.array, b: np.array):
    n = len(A)
    return np.array([b[i] / A[i][i] for i in range(n)])


def solve_simple(A: np.array, b: np.array, epsilon: float, x0: np.array = None, verbosity: int = 0, output: dict = None) -> tuple[np.array, str]:
    alpha = build_alpha(A)
    beta = build_beta(A, b)
    if x0 is None:
        x0 = beta
    x_k_minus_1 = x0
    x_k = build_x_k(alpha, beta, x_k_minus_1)
    error = calc_aposterior(alpha, x_k, x_k_minus_1)
    iter = 1
    while (error > epsilon):
        x_k_minus_1 = x_k
        x_k = build_x_k(alpha, beta, x_k_minus_1)
        error = calc_aposterior(alpha, x_k, x_k_minus_1)
        iter += 1
    if any(np.isnan(x_k)):
        comment = f"Невозможно найти решение; ‖alpha‖ = {np.linalg.norm(alpha)}"
    else:
        comment = f"Решение найдено для ε = {epsilon} за {iter} итераций. " + \
            f"Апостериорная погрешность = {error}"
    if verbosity >= 1:
        print(comment)
    else:
        output.update({"Количество итераций": iter, "comment": comment})
    return x_k


# everywhere below:
# i         — row number in A
# n         — row number in x; often equals to i
# x_U_k     — x^k
# x_i_U_k   — x_i^k
# j_0       — j to start summation with; numbering starts with 0 instead of 1 in the presentations
# max_delta — container needed to populate up the current precision (accessed by ref)
def calc_sum(A: np.array, x_U_k_minus_1: np.array, i: int, j_0: int):
    result = np.dot(A[i][j_0:], x_U_k_minus_1[j_0:]).sum()
    # print(f"sum_result={result}")
    return result


def calc_sum_of_summands(A: np.array, x_U_k: np.array, i: int, n: int):
    if n <= 0:
        return 0.0
    # print(f"summands: x={x_U_k}")
    # print(f"summands: A={A[i][0:n]}, x={x_U_k[0:n]}")
    result = np.dot(A[i][0:n], x_U_k[0:n]).sum()
    # print(f"summands_result={result}")
    return result


def calc_delta_i(A: np.array, b: np.array, x_U_k: np.array, x_U_k_minus_1: np.array, i: int, n: int):
    delta = abs(calc_sum_of_summands(A, x_U_k, i, n) +
                calc_sum(A, x_U_k_minus_1, i, n) - b[i])
    # print(f"δ={delta}, sum={calc_sum(A, x_U_k_minus_1, i, n)}, summands={calc_sum_of_summands(A, x_U_k, i, n)} when i={i}, n={n}")
    return delta


def select_i(A: np.array, b: np.array, x_U_k: np.array, x_U_k_minus_1: np.array, n: int, i_to_ignore: list):
    i_for_max_delta = 0
    max_delta = 0.0
    for i in [j for j in range(len(A)) if j not in i_to_ignore]:
        delta_i = calc_delta_i(A, b, x_U_k, x_U_k_minus_1, i, n)
        if (delta_i > max_delta):
            max_delta = delta_i
            i_for_max_delta = i
    # print(f"i_for_max_δ={i_for_max_delta} when n={n}")
    return i_for_max_delta


# compute and not calc, because it modifies i_to_ignore
def compute_x_n_U_k(A: np.array, b: np.array, x_U_k: np.array, x_U_k_minus_1: np.array, n: int, i_to_ignore: list, max_delta: list):
    i = select_i(A, b, x_U_k, x_U_k_minus_1, n, i_to_ignore)
    i_to_ignore.append(i)
    max_delta.clear()
    max_delta.append(calc_delta_i(A, b, x_U_k, x_U_k_minus_1, i, n))
    sum = calc_sum(A, x_U_k_minus_1, i, n+1)
    summands = calc_sum_of_summands(A, x_U_k, i, n)
    # print(f"sum={sum}, summands={summands}")
    x = (b[i] - sum -
         summands) / A[i][n]
    # print(f"x_n={x} when n={n}")
    return x


def build_x_U_k(A: np.array, b: np.array, x_k_minus_1: np.array, max_delta: list):
    x_U_k = np.array([0.0 for n in range(len(A))])
    i_to_ignore = []
    for n in range(len(A)):
        x_U_k[n] = compute_x_n_U_k(A, b, x_U_k, x_k_minus_1,
                                   n, i_to_ignore, max_delta)
    return x_U_k


def solve_relax(A: np.array, b: np.array, epsilon: float, x_U_0: np.array = None, verbosity: int = 0, output: dict = None) -> tuple[np.array, str]:
    if x_U_0 is None:
        x_U_0 = build_beta(A, b)
    max_delta = []
    x_U_k_minus_1 = x_U_0
    x_U_k = build_x_U_k(A, b, x_U_0, max_delta)
    # print(f"max_δ={max_delta}")
    # print(f"x^k={x_U_k}")
    while (max_delta[0] > epsilon and not (any(np.isnan(x_U_k)) or any(np.isinf(x_U_k)))):
        x_U_k_minus_1 = x_U_k
        x_U_k = build_x_U_k(A, b, x_U_k_minus_1, max_delta)
        # print(f"max_δ={max_delta}")
        if (any(np.isnan(x_U_k)) or any(np.isinf(x_U_k))):
            break
    print(f"x^k={x_U_k}")
    return x_U_k
