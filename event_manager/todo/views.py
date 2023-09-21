from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Todo


def todos(request) -> HttpResponse:
    """Zeige alle Todos in einer Übersicht an.
    
    http://127.0.0.1:8000/todos
    """
    todos = Todo.objects.all()
    return render(
        request,
        "todo/todos.html",
        {
            "todos": todos
        }
    )


def todo_detail(request, pk: int) -> HttpResponse:
    """Zeige eine Todo-Detailseite an.
    
    http://127.0.0.1:8000/todos/2
    """
    # ersetzt try except Block und raise Http404
    todo = get_object_or_404(Todo, pk=pk)

    return render(
        request,
        "todo/todo_detail.html",
        {
           "todo": todo
        }
    )