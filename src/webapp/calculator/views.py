import json
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
import numpy as np

from src.tasks import common_data
from src.tasks.main import get_task_by_number


def index(request):
    def get_matrix_from_json(response: JsonResponse):
        return json.loads(response.content)['A']
    problem_number = 1
    task = get_task_by_number(problem_number)
    context = {
        'problem': problem_number,
        'situation': task.situation(),
        'matrices_available': common_data.SOLE.get_available_matrices_names().items(),
        'matrix': get_matrix_from_json(matrix(request)),
        'answer': json.loads(answer(request).content).items(),
    }
    return render(request, 'calculator/index.html', context)


def matrix(request):
    matrix_name = request.GET.get('matrix')
    if matrix_name is not None:
        A, b = common_data.SOLE.get_SOLE_by_name(matrix_name)
    else:
        A, b = common_data.SOLE.hilbert(2)
    A_lists = A.tolist()
    b_lists = b.tolist()
    return JsonResponse({'A': A_lists, 'b': b_lists})


def answer(request):
    def to_np(response: JsonResponse, field_name: str):
        return np.array(json.loads(response.content)[field_name])
    problem_number = request.GET.get('problem')
    if problem_number is not None:
        problem_number = int(problem_number)
    else:
        problem_number = 1
    response = matrix(request)
    answer = get_task_by_number(problem_number).calc_answer(
        to_np(response, 'A'), to_np(response, 'b'))
    return JsonResponse(json.loads(answer))
