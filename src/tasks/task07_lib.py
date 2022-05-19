import numpy as np
from matplotlib import pyplot as plt
from src.tasks.common_data import SDE


def calc_coeffs(data_from, step):
    [functions, conds, segment] = data_from
    [k, p, q, f] = functions
    [alpha_0, alpha_1, beta_0, beta_1, Ac, Bc] = conds
    [a, b] = segment
    n = round((b - a) / step)
    x = []
    for i in range(n + 1):
        x.append(a + i * step)
    A, B, C, D = [0], [step * alpha_0 - alpha_1], [alpha_1], [step * Ac]
    for i in range(1, n):
        A.append(2 * k(x[i]) - step * p(x[i]))
        B.append(-4 * k(x[i]) + 2 * step ** 2 * q(x[i]))
        C.append(2 * k(x[i]) + step * p(x[i]))
        D.append(2 * step ** 2 * f(x[i]))
    A.append(-beta_1)
    B.append(step * beta_0 + beta_1)
    C.append(0)
    D.append(step * Bc)
    return A, B, C, D


def solve(coeffs):
    [A, B, C, D] = coeffs
    [s, t, u] = [[-C[0]/B[0]], [D[0]/B[0]], [0]]
    n = len(A) - 1
    for i in range(1, len(A)):
        s.append(-C[i] / (A[i] * s[i - 1] + B[i]))
        t.append((D[i] - A[i] * t[i - 1]) / (A[i] * s[i - 1] + B[i]))
        u.append(0)
    u[n] = t[n]
    for i in range(n-1, -1, -1):
        u[i] = s[i] * u[i+1] + t[i]
    return u


def grid(data_from, step, epsilon):
    coeff = 2
    k = 0
    p = 1
    u_k_plus_1 = solve(calc_coeffs(data_from, step))
    while True:
        k += 1
        u_k = u_k_plus_1.copy()
        u_k_plus_1 = solve(calc_coeffs(data_from, step/coeff ** k))
        errors = []
        for i in range(len(u_k)):
            errors.append((u_k_plus_1[2 * i] - u_k[i]) / (coeff ** p - 1))
        if np.linalg.norm(np.array(errors), 2) < epsilon:
            for i in range(len(errors)):
                if i % 2 == 0:
                    u_k_plus_1[2 * i] += errors[i]
                else:
                    u_k_plus_1[i] += (errors[i - 1] + errors[i + 1]) / 2
            x = []
            a = data_from[2][0]
            for i in range(len(u_k_plus_1)):
                x.append(a + i * step / (coeff ** k))
            title = f"Шаг сетки: {step / coeff ** k}, Количество шагов сгущения: {k}"
            return x, u_k_plus_1, title


def draw(name, epsilon):
    data_from = SDE.get_by_name(name)[1:]
    [xs, ys, title] = grid(data_from, step=0.125, epsilon=epsilon)
    plt.plot(xs, ys, color='blue', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.tight_layout()
    return title
