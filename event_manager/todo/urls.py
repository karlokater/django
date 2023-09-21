""" 
Events URLs
"""
from django.urls import path 
from . import views

app_name = "todo"

urlpatterns = [
    # http://127.0.0.1:8000/todos
    path("", views.todos, name="todos"),

    # http://127.0.0.1:8000/todos/3
    path("<int:pk>", views.todo_detail, name="todo_detail"),
]
