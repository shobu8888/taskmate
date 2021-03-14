from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete'),
    path('complete/<task_id>', views.complete_task, name='complete'),
    path('pending/<task_id>', views.pending_task, name='pending'),
    path('edit/<task_id>', views.edit_task, name='edit'),
]
