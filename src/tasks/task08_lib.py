import numpy as np
import scipy as sp
import scipy.integrate
import scipy.misc
import matplotlib.pyplot as plt
from src.tasks.common_data import SDE


class F:
    def __init__(self, function, name):
        self.f = function
        self.name = name
        self.df = lambda t: sp.misc.derivative(self.f, t)
        self.ddf = lambda t: sp.misc.derivative(self.df, t)


def build_jacobi_polynomial(n, k):
    return F(lambda t: (1-t**2) * sp.special.eval_jacobi(n, k, k, t), "Jacobi polynomial")


def A_i(functions, phi_i):
    [k, p, q, *_] = functions
    return lambda x: k(x) * phi_i.ddf(x) + p(x) * phi_i.df(x) + q(x) * phi_i.f(x)


def solve_galerkin(data_from, N):
    functions, conditions, interval = data_from
    f = functions[3]
    [a, b] = interval
    phi = [build_jacobi_polynomial(i, 1) for i in range(N)]
    A = np.array([A_i(functions, phi[i]) for i in range(N)])
    B = np.array([sp.integrate.quad(lambda t: phi[i].f(t) * A[j](t), a, b)[0]
                  for i in range(N) for j in range(N)]).reshape((N, N))
    C = np.array([sp.integrate.quad(lambda t: f(t) * phi[i].f(t), a, b)[0]
                 for i in range(N)])
    alpha = np.linalg.solve(B, C)
    return lambda t: sum([alpha[i] * phi[i].f(t) for i in range(N)])


def get_graph_data(data_from, config):
    [N, h] = config
    u = solve_galerkin(data_from, N)
    a, b = data_from[2]
    n = round((b - a) / h)
    x = [a + i * h for i in range(n + 1)]
    y = [u(x[i]) for i in range(n + 1)]
    title = f"N = {N}, h = {h}"
    return x, y, title


def draw(name, test_case):
    data_from = SDE.get_by_name(name)[1:]
    [xs, ys, title] = get_graph_data(data_from, test_case)
    plt.plot(xs, ys, ".-", color='blue', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.tight_layout()
    return title
