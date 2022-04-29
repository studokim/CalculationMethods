import numpy as np

MAX_ITER = 5000


def solve_power(A, x_0, epsilon):
    x_k_minus_1 = x_0
    x_k = np.dot(A, x_0)
    lambda_k = (x_k[0] / x_k_minus_1[0])
    iter = 1
    while (iter < MAX_ITER):
        x_k_minus_1 = x_k
        x_k = np.dot(A, x_k)
        lambda_k_minus_1 = lambda_k
        lambda_k = (x_k[0] / x_k_minus_1[0])
        iter += 1
        if (abs(lambda_k - lambda_k_minus_1) < epsilon):
            break
    return abs(lambda_k), iter


def solve_scalar(A, x_0, epsilon):
    x_k_minus_1 = x_0
    x_k = np.dot(A, x_0)
    y_k = np.dot(A.T, x_k_minus_1)
    lambda_k = np.dot(x_k.T, y_k) / np.dot(x_k_minus_1.T, y_k)
    iter = 1
    while (iter < MAX_ITER):
        x_k_minus_1 = x_k
        x_k = np.dot(A, x_k)
        y_k = np.dot(A.T, y_k)
        lambda_k_minus_1 = lambda_k
        lambda_k = np.dot(x_k.T, y_k) / np.dot(x_k_minus_1.T, y_k)
        iter += 1
        if (abs(lambda_k - lambda_k_minus_1) < epsilon):
            break

    return np.abs(lambda_k), iter
