import numpy as np


def compute_aposterior(alpha: np.array, x_k: np.array, x_k_minus_1: np.array):
    alpha_norm = np.linalg.norm(alpha)
    error = np.linalg.norm(x_k - x_k_minus_1) * \
        alpha_norm / abs(1 - alpha_norm)
    return error


def build_x_k(alpha: np.array, beta: np.array, x_k_minus_1: np.array):
    return beta + np.dot(alpha, x_k_minus_1)


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


def solve_simple(A: np.array, b: np.array, epsilon: float, x0: np.array = None, verbosity: int = 0):
    alpha = build_alpha(A)
    beta = build_beta(A, b)
    if x0 is None:
        x0 = beta
    x_k_minus_1 = x0
    x_k = build_x_k(alpha, beta, x_k_minus_1)
    error = compute_aposterior(alpha, x_k, x_k_minus_1)
    iter = 1
    while (error > epsilon):
        x_k_minus_1 = x_k
        x_k = build_x_k(alpha, beta, x_k_minus_1)
        error = compute_aposterior(alpha, x_k, x_k_minus_1)
        iter += 1
    if verbosity >= 1:
        if any(np.isnan(x_k)):
            print(
                f"Невозможно найти решение; ‖alpha‖ = {np.linalg.norm(alpha)}")
        else:
            print(f"Решение найдено для ε = {epsilon} за {iter} итераций.")
            print(f"Апостериорная погрешность = {error}")
    return x_k
