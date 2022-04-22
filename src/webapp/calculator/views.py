from django.shortcuts import render

from src.tasks import common_data
from src.tasks import task01, task02, task04


def index(request):
    matrix_name = request.GET.get('matrices')
    if matrix_name is not None:
        matrix = common_data.SOLE.get_matrix_by_name(matrix_name)
    else:
        matrix = common_data.SOLE.hilbert(2)[0]
    context = {
        'problem': 1,
        'situation': task01.situation(),
        'matrices_available': common_data.SOLE.get_available_matrices_names().items(),
        'matrix': matrix,
    }
    return render(request, 'calculator/index.html', context)
