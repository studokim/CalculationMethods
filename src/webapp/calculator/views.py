import json
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

from src.tasks.common_tasks import *
from src.tasks.common_lib import is_base64
from .forms import get_form_by_number, get_params_by_number


def index(request):
    context = {
        'solved_tasks': get_solved_tasks().items(),
        'unsolved_tasks': get_unsolved_tasks().items(),
    }
    return render(request, 'calculator/index.html', context)


def task(request, task_id):
    if request.method == 'POST':
        form = get_form_by_number(task_id)(request.POST)
    else:
        form = get_form_by_number(task_id)
    context = {
        'task_id': task_id,
        'situation': get_task_by_number(task_id).situation(),
        'form': form,
        'params_template': f'calculator/params/{task_id}.html',
    }
    return render(request, 'calculator/task.html', context)


def params(request, task_id):
    try:
        form = get_form_by_number(task_id)(request.POST)
        parsed_params = get_params_by_number(task_id, form)
        return JsonResponse(parsed_params)
    except:
        return JsonResponse({'error': 'form invalid'})


def rendered_params(request, task_id):
    context = json.loads(request.body)
    return render(request, f'calculator/params/{task_id}.html', context)


def answer(request: HttpRequest, task_id):
    try:
        parsed_params = json.loads(request.body)
        answer = get_task_by_number(task_id).calc_answer(parsed_params)
        return JsonResponse(json.loads(answer))
    except:
        return JsonResponse({'error': 'params invalid'})


def rendered_answer(request, task_id):
    context = {
        'answer': filter(lambda pair: not is_base64(pair[1]), json.loads(request.body).items()),
        'answer_base64': filter(lambda pair: is_base64(pair[1]), json.loads(request.body).items()),
    }
    return render(request, f'calculator/answer.html', context)
