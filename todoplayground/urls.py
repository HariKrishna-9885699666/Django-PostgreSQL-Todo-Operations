from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos, name='todos'),
    path('todos/delete/<int:task_id>/', views.todos, name='delete_task'),
    path('todos/edit/<int:task_id>/', views.todos, name='edit_task'),
    path('todos/complete/<int:task_id>/', views.complete_todo, name='complete_todo'),
    path('', views.todos, name='todos'),
]