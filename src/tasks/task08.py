import json
from src.tasks.common_lib import *
from src.tasks.task08_lib import *


def situation():
    return ["Реализовать один из проекционных методов: метод Ритца или метод Галеркина.",
            "Условия можно взять в [5]. Сравнить решения при разных N",
            "(либо графически, либо выводить значения решений на достотачно частой сетке)."]


def calc_answer(params: dict):
    name = params['name']
    enable_plotting()
    test_cases = [
        [1, 0.05],
        [3, 0.04],
        [5, 0.03],
        [8, 0.01]
    ]
    answer = {}
    for test_case in test_cases:
        answer.update({draw(name, test_case): get_plot()})
        plt.cla()
    return json.dumps(answer, ensure_ascii=False)


def main():
    print_task(8)
    print(calc_answer({"name": "third", "epsilon": 0.01}))


if __name__ == '__main__':
    main()
