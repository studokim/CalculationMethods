import numpy as np
from src.tasks.task01_lib import build_hilbert


class SOLE:
    def hilbert(n: int):
        return build_hilbert(n), np.array([1 for i in range(n)])

    def pakulina_2():
        # матрица из Пакулиной, стр. 90, вар. 1
        A = np.array([[-400.60, 199.80],
                      [1198.80, -600.40]])
        b = np.array([200, -600])
        return A, b

    def pakulina_3():
        # матрица из Пакулиной, стр. 94, вар. 1
        A = np.array([[3.278164, 1.046583, -1.378574],
                      [1.046583, 2.975937, 0.934251],
                      [-1.378574, 0.934251, 4.836173]])
        b = np.array([-0.527466, 2.526877, 5.165441])
        return A, b

    def tridiag_5():
        # матрица трёхдиагональная
        A = np.array([[1, 12, 0, 0, 0],
                      [13, 14, 5, 0, 0],
                      [0, 0, 16, 0, 0],
                      [0, 0, 7, 18, 1/9],
                      [0, 0, 0, 0, 10]])
        b = np.array([1, 1, 1, 1, 1])
        return A, b

    def tridiag_7():
        # матрица трёхдиагональная
        A = np.array([[1, 12, 0, 0, 0, 0, 0],
                      [13, 14, 5, 0, 0, 0, 0],
                      [0, 0, 16, 88, 0, 0, 0],
                      [0, 0, 11, 9, 0, 0, 0],
                      [0, 0, 0, 1/7, 77, 7, 0],
                      [0, 0, 0, 0, 1, 1/9, 1],
                      [0, 0, 0, 0, 0, 0, 999]])
        b = np.array([1, 1, 1, 1, 1, 1, 1])
        return A, b
