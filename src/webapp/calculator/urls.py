from django.urls import path

from . import views

app_name = 'calculator'
urlpatterns = [
    # ex: /calculator/
    path('', views.index, name='index'),
    # ex: /calculator/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
