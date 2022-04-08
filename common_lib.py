current_test = 1


def print_test(name: str = ""):
    global current_test
    print(f"\nТест {current_test}. {name}")
    current_test += 1


def print_task(number: int):
    print(f"##### Задача {number} #####")
