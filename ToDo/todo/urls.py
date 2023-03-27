from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='index'),
    path('todo/', views.todo_index, name='todoList'),
    path('todo/<id>/delete', views.todo_delete, name='delete'),
    path('todo/<id>/edit', views.todo_edit, name='edit'),
    path('todo/create', views.todo_create, name='create')
]