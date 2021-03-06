import json
from src.tasks.common_lib import *
from src.tasks.common_data import SOLE
from src.tasks.task01_lib import calc_diff
from src.tasks.task04_lib import *
from src.tasks.task02_lib import print_diff


def situation():
    return ["Реализовать решение СЛАУ двумя итерационными методами:",
            "- методом простой итерации",
            "- методом Зейделя или методом релаксации.",
            "Сравнить количество итераций.",  # <----------------------------------------------
            "Находить решения с разной точностью (т.е. варьировать ε, до достижения которого проводятся итерации).",
            "Может быть между ε и количеством итераций k есть зависимость?",
            "Примечание: поскольку релаксационные методы используют",
            "более “свежую” информацию о сделанных преобразованиях,",
            "то обычно они сходятся быстрее метода простой итерации.",  # <------------------------
            "Протестировать работу методов на плохо обусловленных матрицах —",
            "например, на примере из методички А.Н.Пакулиной и на матрице Гильберта (см. задание 1).",
            "Если есть возможность — протестировать работу методов на",
            "симметричных с диагональным преобладанием разреженных матрицах большого порядка (больше 200).",
            "Реализация метода релаксации с тестированием на больших разреженных матрицах дает дополнительный “плюсик”."]


def calc_answer(params: dict):
    A = np.array(params['A'])
    b = np.array(params['b'])
    epsilon = float(params['epsilon'])
    output = {}
    X = solve_simple(A, b, epsilon, output=output)
    X_seidel = solve_seidel(A, b, epsilon, output=output)
    X_bib = np.linalg.solve(A, b)
    answer = {
        # NaNs are unexpected characters when dumping to json
        "X, полученный методом простой итерации": str(X),
        "X, полученный методом Зейделя": str(X_seidel),
        "X, полученный библиотечной функцией": str(X_bib),
        "|X - X_bib|": str(calc_diff(X, X_bib)),
        "|X_seidel - X_bib|": str(calc_diff(X_seidel, X_bib)),
        "A * X": str(np.dot(A, X)),
        "A * X_bib": str(np.dot(A, X_seidel)),
    }
    answer.update(output)
    return json.dumps(answer, ensure_ascii=False)


def print_answer(A: np.array, b: np.array):
    epsilon = 10**(-4)
    X = solve_simple(A, b, epsilon, verbosity=1)
    X_ = np.linalg.solve(A, b)
    X_seidel = solve_seidel(
        A, b, epsilon, [0.0 for i in range(len(A))])
    print_diff(X, X_)


def main():
    print_task(4)

    print_test("Из machinelearning")
    A = np.array([[1.0, 1.0], [1.0, 3.0]])
    b = np.array([3.0, 7.0])
    print_answer(A, b)

    # print_test("Из 0..3")
    # A = np.array([[3.0, 1.0], [2.0, 3.0]])
    # b = np.array([1.0, 1.0])
    # print_answer(A, b)

    # print_test("Гильберта 2-го порядка")
    # A, b = SOLE.hilbert(2)
    # print_answer(A, b)

    # print_test("Гильберта 3-го порядка")
    # A, b = SOLE.hilbert(3)
    # print_answer(A, b)

    # print_test("Гильберта 10-го порядка")
    # A, b = SOLE.hilbert(10)
    # print_answer(A, b)

    # # матрица из Пакулиной, стр. 90, вар. 1
    # print_test()
    # A, b = SOLE.pakulina(2)
    # print_answer(A, b)

    # # матрица из Пакулиной, стр. 94, вар. 1
    # print_test()
    # A, b = SOLE.pakulina(3)
    # print_answer(A, b)


if __name__ == '__main__':
    main()
