from random import choice
import numpy as np
from copy import deepcopy

k_bad_cond = 10**4


def print_cond(cond: float, name: str = "???"):
    if cond > k_bad_cond:
        print(f"{name:7} cond = {cond}. Плохо обусловлена!")
    else:
        print(f"{name:7} cond = {cond}")


def compute_diff(X: np.array, X_: np.array):
    return np.linalg.norm(X - X_)


def print_diff(X: np.array, X_: np.array, delta: float):
    diff = compute_diff(X, X_)
    print(f"X  = {X} исходный")
    print(f"X_ = {X_} после вариации на {delta}")
    print(f"|X - X_| = {diff}")


# спектральный критерий обусловленности
def compute_cond_s(A: np.array):
    cond = np.linalg.norm(A) * np.linalg.norm(np.linalg.inv(A))
    return cond


# объёмный критерий обусловленности
def compute_cond_v(A: np.array):
    cond = 1
    for row in A:
        sum = 0
        for anm in row:
            sum += anm**2
        cond *= sum**(1/2)
    cond /= np.linalg.det(A)
    return cond


# угловой критерий обусловленности
def compute_cond_a(A: np.array):
    cond = 0
    A_inv = np.linalg.inv(A)
    A_inv = np.transpose(A_inv)
    for n in range(len(A)):
        a = np.linalg.norm(A[n])
        c = np.linalg.norm(A_inv[n])
        cond = max(cond, a*c)
    return cond


def probe():
    return choice([0, 1])


def sign():
    return choice([-1, 1])


def build_variated(A: np.array, delta: float):
    A_ = deepcopy(A)
    for row in range(len(A)):
        for col in range(len(A)):
            if (probe()):
                A_[row][col] += sign() * delta
    return A_


def build_hilbert(n: int):
    return np.array([[1/i for i in range(row_start, row_start + n)]
                    for row_start in range(1, n + 1)])
