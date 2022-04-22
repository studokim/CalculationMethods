import numpy as np
from src.tasks.task01_lib import build_hilbert


class SOLE:
    def get_matrix_by_name(name: str) -> callable:
        method_name = name.split("_")[0]
        n = int(name.split("_")[1])
        method = getattr(SOLE, method_name)
        return method(n)[0]

    def get_available_matrices_names() -> dict:
        return {
            "hilbert_2": "Гильберта порядка 2",
            "hilbert_3": "Гильберта порядка 3",
            "hilbert_6": "Гильберта порядка 6",
            "hilbert_10": "Гильберта порядка 10",
            "hilbert_20": "Гильберта порядка 20",
            "pakulina_2": "Пакулиной порядка 2",
            "pakulina_3": "Пакулиной порядка 3",
            "tridiag_5": "Трёхдиагональная порядка 5",
            "tridiag_7": "Трёхдиагональная порядка 7",
        }

    def hilbert(n: int):
        return build_hilbert(n), np.array([1 for i in range(n)])

    def pakulina(n: int):
        match n:
            case 2:
                # матрица из Пакулиной, стр. 90, вар. 1
                A = np.array([[-400.60, 199.80],
                              [1198.80, -600.40]])
                b = np.array([200, -600])
            case 3:
                # матрица из Пакулиной, стр. 94, вар. 1
                A = np.array([[3.278164, 1.046583, -1.378574],
                              [1.046583, 2.975937, 0.934251],
                              [-1.378574, 0.934251, 4.836173]])
                b = np.array([-0.527466, 2.526877, 5.165441])
            case _:
                raise
        return A, b

    def tridiag(n: int):
        match n:
            case 5:
                # матрица трёхдиагональная
                A = np.array([[1, 12, 0, 0, 0],
                              [13, 14, 5, 0, 0],
                              [0, 0, 16, 0, 0],
                              [0, 0, 7, 18, 1/9],
                              [0, 0, 0, 0, 10]])
                b = np.array([1, 1, 1, 1, 1])
            case 7:
                # матрица трёхдиагональная
                A = np.array([[1, 12, 0, 0, 0, 0, 0],
                              [13, 14, 5, 0, 0, 0, 0],
                              [0, 0, 16, 88, 0, 0, 0],
                              [0, 0, 11, 9, 0, 0, 0],
                              [0, 0, 0, 1/7, 77, 7, 0],
                              [0, 0, 0, 0, 1, 1/9, 1],
                              [0, 0, 0, 0, 0, 0, 999]])
                b = np.array([1, 1, 1, 1, 1, 1, 1])
            case _:
                raise
        return A, b
