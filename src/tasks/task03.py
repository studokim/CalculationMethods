import json
from src.tasks.common_lib import *
from src.tasks.common_data import SOLE
from src.tasks.task01_lib import calc_cond_s, calc_diff
from src.tasks.task02_lib import solve
from src.tasks.task03_lib import *


def situation():
    return ["Реализовать метод решения СЛАУ, на выбор: метод вращений или метод отражений.",
            "Вычислить числа обусловленности. Протестировать на тех же матрицах, что использовались в задании 2; сравнить."]


def calc_answer(params: dict):
    A = np.array(params['A'])
    b = np.array(params['b'])

    Q, R, b_i = build_QR(A, b)
    X = solve(A, b)
    X_bib = np.linalg.solve(A, b)
    X_i_bib = np.linalg.solve(R, b_i)
    diff = calc_diff(X, X_i_bib)

    cond = calc_cond_s(A)
    answer = {
        "Число обусловленности матрицы A": cond,
        "Матрица Q": str(Q),
        "Матрица R": str(R),
        "Число обусловленности матрицы Q": calc_cond_s(Q),
        "Число обусловленности матрицы R": calc_cond_s(R),
        "Задача плохо обусловлена?": int(cond > k_bad_cond),
        "X": X.tolist(),
        "X, полученный библиотечной функцией": X_bib.tolist(),
        "|X - X_bib|": diff,
        "A * X": str(np.dot(A, X)),
        "A * X_bib": str(np.dot(A, X_bib)),
    }
    return json.dumps(answer, ensure_ascii=False)


def main():
    print_task(3)

    print_test("Гильберта 3-го порядка")
    A, b = SOLE.hilbert(3)
    calc_answer(A, b)


if __name__ == '__main__':
    main()
