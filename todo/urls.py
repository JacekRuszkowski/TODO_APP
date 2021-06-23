from django.contrib import admin
from django.urls import path, include
from .views import (
    tasks_view,
    add_task,
    AddBoard,
    DeleteBoard,
    DeleteTask,
    task_status,
    edit_task,
    edit_board
)

urlpatterns = [
    path('', tasks_view, name='tasks-view'),
    path('<pk>/add-task/', add_task, name='add-task'),
    path('add-board/', AddBoard.as_view(), name='add-board'),
    path('<pk>/edit-board', edit_board, name='edit-board'),
    path('<pk>/delete-board/', DeleteBoard.as_view(success_url='/'), name='delete-board'),
    path('<pk>/delete-task/', DeleteTask.as_view(success_url='/'), name='delete-task'),
    path('<pk>/task-status/', task_status, name='task-status'),
    path('<pk>/edit-task', edit_task, name='edit-task')
]

