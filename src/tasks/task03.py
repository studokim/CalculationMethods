import json
from src.tasks.common_lib import *
from src.tasks.common_data import SOLE
from src.tasks.task01_lib import calc_cond_s, print_cond
from src.tasks.task02_lib import *


def situation():
    return ["Реализовать метод решения СЛАУ, на выбор:",
            "LU-разложение или метод квадратного корня.",
            "Для матриц A, L, U вычислить числа обусловленности.",
            "Протестировать на разных матрицах:",
            "хорошо обусловленных, [очень] плохо обусловленных.",
            "Для нескольких плохо обусловленных матриц",
            "(например, для матриц Гильберта разного, больше 15, порядка)",
            "реализовать метод регуляризации:",
            "параметр α варьировать в пределах от 10−12 до 10−1 ;",
            "для каждого конкретного значения α найти числа обусловленности",
            "(матриц A + αE ) и норму погрешности получившегося решения;",
            "понять, какое значение α = α в каждом конкретном случае",
            "(= для каждой конкретной матрицы) кажется наилучшим.",
            "Наилучшее α можно находить из предположений, что точным решением является",
            "- вектор x0 = (1,1,...,1);",
            "- случайный вектор x0.",
            "Проверить результат на [другом] случайном векторе x0."]


def calc_answer(params: dict):
    A = np.array(params['A'])
    b = np.array(params['b'])
    L, U = build_LU(A)
    cond = calc_cond_s(A)
    X = solve(A, b)
    X_bib = np.linalg.solve(A, b)
    X_ = None
    X0 = None
    X_test = None
    diff_regularized = None
    if (cond > k_bad_cond):
        X_ = solve_regularizing(A, b)
        X0 = build_random_vector(len(A))
        X_test = solve_regularizing(A, b, X0)
        diff_regularized = calc_diff(X_, X_test)
        X_ = X_.tolist()
        X0 = X0.tolist()
        X_test = X_test.tolist()
    answer = {
        "Число обусловленности матрицы A": cond,
        "Число обусловленности матрицы L": calc_cond_s(L),
        "Число обусловленности матрицы U": calc_cond_s(U),
        "Задача плохо обусловлена?": int(cond > k_bad_cond),
        "X, полученный библиотечной функцией": X_bib.tolist(),
        "X": X.tolist(),
        "|X - X_bib|": calc_diff(X, X_bib),
        "X, полученный методом регуляризации": X_,
        "X0": X0,
        "X проверочный": X_test,
        "|X_reg - X_prov|": diff_regularized,
    }
    return json.dumps(answer, ensure_ascii=False)


def print_answer(A: np.array, b: np.array):
    L, U = build_LU(A)
    cond = calc_cond_s(A)
    print_cond(cond, "A:")
    print_cond(calc_cond_s(L), "L:")
    print_cond(calc_cond_s(U), "U:")
    x = solve(A, b)
    x_bib = np.linalg.solve(A, b)
    print_diff(x, x_bib)
    if (cond > k_bad_cond):
        x_ = solve_regularizing(A, b, verbosity=2)
        x0 = build_random_vector(len(A))
        print(f"Проверим результат на {x0}:")
        x_test = solve_regularizing(A, b, x0, verbosity=1)
        print_diff(x_, x_test, "решение методом регуляризации",
                   "проверочное решение")


def main():
    print_task(2)

    print_test("Гильберта 3-го порядка")
    A, b = SOLE.hilbert(3)
    print_answer(A, b)

    print_test("Гильберта 10-го порядка")
    A, b = SOLE.hilbert(10)
    print_answer(A, b)

    print_test("Гильберта 20-го порядка")
    A, b = SOLE.hilbert(20)
    print_answer(A, b)

    print_test()
    A, b = SOLE.pakulina(3)
    print_answer(A, b)


if __name__ == '__main__':
    main()
