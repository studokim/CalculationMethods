from django.urls import path

from . import views

app_name = 'calculator'
urlpatterns = [
    path('', views.index, name='index'),
    path('matrix', views.matrix, name='matrix'),
    path('answer', views.answer, name='answer'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
