import json
from src.tasks.common_data import SOLE
from src.tasks.common_lib import print_task, print_test
from src.tasks.task01_lib import *


def situation():
    return [
        "Для СЛАУ с некоторой матрицей A вычислить числа обусловленности;",
        "поварьировав матрицу и правую часть (например, на 10−2..10−10), вычислить |x − x̃|",
        "посмотреть, есть ли корреляция между величинами чисел обусловленности и погрешностью решения.",
        "Для тестов можно брать:",
        "- матрицы Гильберта разного порядка (например, от 3 до 10)",
        "- системы из методички А.Н.Пакулиной, часть 1",
        "- какие-нибудь хорошие матрицы (например, трехдиагональные с диагональным преобладанием)."]
# Статья, в которой предлагается метод подсчёта углового числа обусловленности: https://elibrary.ru/download/elibrary_15524850_60661752.pdf


def calc_answer(params: dict):
    A = np.array(params['A'])
    b = np.array(params['b'])
    delta = float(params['delta'])
    cond_s = calc_cond_s(A)
    cond_v = calc_cond_v(A)
    cond_a = calc_cond_a(A)
    A_ = build_variated(A, delta)
    X = np.linalg.solve(A, b)
    X_ = np.linalg.solve(A_, b)
    answer = {
        "Спектральное число обусловленности": cond_s,
        "Объёмное число обусловленности": cond_v,
        "Угловое число обусловленности": cond_a,
        "Задача плохо обусловлена?": int(cond_s > k_bad_cond or cond_v > k_bad_cond or cond_a > k_bad_cond),
        "δ": delta,
        "X": X.tolist(),
        "X после вариации": X_.tolist(),
        "|X - X_var|": calc_diff(X, X_),
    }
    return json.dumps(answer, ensure_ascii=False)


def print_answer(A: np.array, b: np.array):
    print_cond(calc_cond_s(A), "spectre")
    print_cond(calc_cond_v(A), "volume")
    print_cond(calc_cond_a(A), "angle")
    X = np.linalg.solve(A, b)
    delta = 10**(-4)
    A_ = build_variated(A, delta)
    X_ = np.linalg.solve(A_, b)
    print_diff(X, X_, delta)


def main():
    print_task(1)

    print_test("Гильберта 3-го порядка")
    A, b = SOLE.hilbert(3)
    print_answer(A, b)

    print_test("Гильберта 6-го порядка")
    A, b = SOLE.hilbert(6)
    print_answer(A, b)

    print_test("Гильберта 10-го порядка")
    A, b = SOLE.hilbert(10)
    print_answer(A, b)

    # матрица из Пакулиной, стр. 90, вар. 1
    print_test()
    A, b = SOLE.pakulina(2)
    print_answer(A, b)

    # матрица из Пакулиной, стр. 94, вар. 1
    print_test()
    A, b = SOLE.pakulina(3)
    print_answer(A, b)

    print_test("Трёхдиагональная")
    A, b = SOLE.tridiag(5)
    print_answer(A, b)

    print_test("Трёхдиагональная")
    A, b = SOLE.tridiag(7)
    print_answer(A, b)


if __name__ == '__main__':
    main()
