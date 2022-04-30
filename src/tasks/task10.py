import json
from src.tasks.common_lib import *
from src.tasks.task10_lib import *


def situation():
    return ["Реализовать решение уравнения теплопроводности по двум схемам: одной из неявных и явной.",
            "Посмотреть на поведение решения по явной схеме при несоблюдении условий устойчивости.",
            "Результаты выводить либо графически (поверхность), либо численно (матрицу значений). Условия задач можно взять в [2]"]


def calc_answer(params: dict):
    name = params['name']
    explicit = (params['explicit'] == "True")
    enable_plotting()
    draw(name, explicit)
    answer = {
        "img": get_plot()
    }
    return json.dumps(answer, ensure_ascii=False)


def main():
    print_task(10)
    print(calc_answer({"name": "1", "explicit": True}))


if __name__ == '__main__':
    main()
