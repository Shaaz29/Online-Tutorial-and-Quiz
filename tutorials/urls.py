from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [
    path('', views.tutorial_list, name='tutorial_list'),
    path('<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
    path('quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
]
