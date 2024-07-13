from django.urls import path
from task.views import home_view, task_done_view, task_delete_view, done_delete_task_view, search, create_task, \
    delete_task, edit_task

urlpatterns = [
    path('', home_view, name='home-view'),

    path('task-done-view/', task_done_view, name='task-done-view'),
    path('task-deleted-view/', task_delete_view, name='task-delete-view'),
    path('done-deleted-task-view/', done_delete_task_view, name='done-delete-task-view'),

    path('search/', search, name='search-task'),

    path('create-task/', create_task, name='create-task'),

    path('edit-task/', edit_task, name='edit-task'),
    path('delete-task/', delete_task, name='delete-task')
]
