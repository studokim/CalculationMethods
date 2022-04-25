from django.urls import path

from . import views

app_name = 'calculator'
urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>', views.task, name='task'),
    path('task/<int:task_id>/params', views.params, name='params'),
    path('task/<int:task_id>/rendered_params',
         views.rendered_params, name='rendered_params'),
    path('task/<int:task_id>/answer', views.answer, name='answer'),
    path('task/<int:task_id>/rendered_answer',
         views.rendered_answer, name='rendered_answer'),

]
