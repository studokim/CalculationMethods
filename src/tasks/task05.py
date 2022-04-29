import json
from src.tasks.common_lib import *
from src.tasks.task05_lib import *


def situation():
    return ["Реализовать для нахождения максимального по модулю собственного числа и соответствующего собственного вектора матрицы",
            "- степенной метод и",
            "- метод скалярных произведений.",
            "Вычисления проводить до достижения точности ε. Варьируя ε, скажем, от 10−2 до 10−5 , изучить зависимость количества итераций от ε.",
            "Сравнить количество итераций в методах (при каждом фиксированном ε).",
            "Некоторые источники примеров матриц: методичка А.Н. Пакулиной, учебник Д.К. Фаддевва и В.Н. Фаддеевой, матрицы Гильберта разного порядка",
            "Если есть возможность — сравнить полученные значения (с.ч. и с.в.) с найденными встроенными функциями."]


def calc_answer(params: dict):
    A = np.array(params['A'])
    x_0 = np.array(list(map(float, params['x_0'])))
    epsilon = float(params['epsilon'])
    max_lambda_pow, iter_pow = solve_power(A, x_0, epsilon)
    max_lambda_scal, iter_scal = solve_scalar(A, x_0, epsilon)
    eigenvectors = np.linalg.eig(A)
    answer_bib = []
    for i in range(len(eigenvectors[0])):
        answer_bib.append(
            f"λ={eigenvectors[0][i]}, v={eigenvectors[1][i]}")
    answer = {
        "СЧ и СВ, полученные библиотечной функцией": "; ".join(answer_bib),
        "λ_max, полученное степенным методом": max_lambda_pow,
        "Количество итераций степенного метода": iter_pow,
        "λ_max, полученное методом скалярных произведений": max_lambda_scal,
        "Количество итераций метода скалярных произведений": iter_scal
    }
    return json.dumps(answer, ensure_ascii=False)


def main():
    print_task(5)

    print_test("Из machinelearning")
    A = np.array([[1.0, 1.0], [1.0, 3.0]])
    epsilon = 0.0001
    print(calc_answer({"A": A, "x_0": ["0.2", "0.1"], "epsilon": epsilon}))

    # print_test("Из 0..3")
    # A = np.array([[3.0, 1.0], [2.0, 3.0]])
    # b = np.array([1.0, 1.0])
    # print(calc_answer({"A":A, "b":b}))

    # print_test("Гильберта 2-го порядка")
    # A, b = SOLE.hilbert(2)
    # print(calc_answer({"A":A, "b":b}))

    # print_test("Гильберта 3-го порядка")
    # A, b = SOLE.hilbert(3)
    # print(calc_answer({"A":A, "b":b}))

    # print_test("Гильберта 10-го порядка")
    # A, b = SOLE.hilbert(10)
    # print(calc_answer({"A":A, "b":b}))

    # # матрица из Пакулиной, стр. 90, вар. 1
    # print_test()
    # A, b = SOLE.pakulina(2)
    # print(calc_answer({"A":A, "b":b}))

    # # матрица из Пакулиной, стр. 94, вар. 1
    # print_test()
    # A, b = SOLE.pakulina(3)
    # print(calc_answer({"A":A, "b":b}))


if __name__ == '__main__':
    main()
