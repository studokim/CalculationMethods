from django.shortcuts import render
from django.http import HttpResponse

from src.tasks import common_data


def index(request):
    context = {
        'matrix': common_data.SOLE.hilbert(3),
    }
    return render(request, 'calculator/index.html', context)
