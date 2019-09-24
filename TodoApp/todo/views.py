from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Todo

# Create your views here.
def todos(request):
    todos = Todo.objects.order_by('-todo_date')
    data = {
        "todos": list(todos.values(
            "todo_subject", "check"
        ))
    }
    return JsonResponse(data)


def todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    data = {
        "todo_subject": todo.todo_subject,
        "todo_details": todo.todo_details,
        "todo_date":todo.todo_date,
        "check":todo.check
    }
    return JsonResponse(data)




