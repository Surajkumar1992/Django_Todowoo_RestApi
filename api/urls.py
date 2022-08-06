from django.urls import path
from . import views

urlpatterns = [
    path('todos', views.TodosList.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),
    path('todos/current', views.TodoCurrentList.as_view()),
    path('todos/important', views.TodoImportantList.as_view()),
]
