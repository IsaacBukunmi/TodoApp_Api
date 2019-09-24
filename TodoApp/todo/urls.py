from django.urls import path

from .import views

urlpatterns = [
    path('', views.todos, name="todos"),
    path('<int:todo_id>', views.todo, name="todo"),
]