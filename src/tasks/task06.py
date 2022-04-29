import json
from src.tasks.common_lib import *
from src.tasks.task06_lib import *


def situation():
    return ["Реализовать метод Якоби поиска всех собственных чисел. Использовать две какие-либо стратегии выбора обнуляемого элемента.",
            "Вычисления проводить до достижения точности ε. Варьируя ε, скажем, от 10−2 до 10−5 , изучить зависимость количества итераций от ε.",
            "Обязательно протестировать на матрице Гильберта порядка > 5. Выводить количество итераций.",
            "По теореме Гершгорина определить область, в которую должны попадать с.ч. матрицы.",
            "Проверить, действительно ли найденные значения в область попали.",
            "Некоторые источники примеров матриц: методичка А.Н. Пакулиной, учебник Д.К. Фаддевва и В.Н. Фаддеевой, матрицы Гильберта разного порядка",
            "Сравнить результаты заданий 5 и 6. Если есть возможность — сравнить полученные значения (с.ч. и с.в.) с найденными встроенными функциями."]


def calc_answer(params: dict):
    A = np.array(params['A'])
    epsilon = float(params['epsilon'])

    lambdas_bib = np.array(sorted(np.linalg.eigvals(A), key=lambda l: abs(l)))
    lambdas_me, iter_me = solve(A, epsilon, Strategy.MAX_ELEMENT)
    lambdas_cc, iter_cc = solve(A, epsilon, Strategy.CYCLE_CHOICE)
    diff_me = calc_diff(lambdas_bib, lambdas_me)
    diff_cc = calc_diff(lambdas_bib, lambdas_cc)

    are_in_gershgorin_circle = True
    for lambda_k in lambdas_me:
        if not is_in_gershgorin_circle(A, lambda_k):
            are_in_gershgorin_circle = False
            break
    answer = {
        "λ, найденные библиотечной функцией": str(lambdas_bib),
        "λ, найденные по стратегии max элемента": str(lambdas_me),
        "λ, найденные по стратегии циклического выбора": str(lambdas_cc),
        "diff_me": diff_me,
        "diff_cc": diff_cc,
        "λ лежат в кругах Гершгорина": are_in_gershgorin_circle,
        "Количество итераций по стратегии max элемента": iter_me,
        "Количество итераций по стратегии циклического выбора": iter_cc,
    }
    return json.dumps(answer, ensure_ascii=False)


def main():
    print_task(6)

    print(calc_answer({"A": A, "epsilon": epsilon}))

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
