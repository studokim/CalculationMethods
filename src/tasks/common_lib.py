import base64
from email.mime import base
from matplotlib import pyplot
from io import BytesIO
import re


current_test = 1


def print_test(name: str = ""):
    global current_test
    print(f"\nТест {current_test}. {name}")
    current_test += 1


def print_task(number: int):
    print(f"##### Задача {number} #####")


def get_plot():
    buffer = BytesIO()
    pyplot.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def enable_plotting():
    pyplot.switch_backend('AGG')


def is_base64(string: str):
    try:
        base64.b64decode(string)
        return True
    except:
        return False
