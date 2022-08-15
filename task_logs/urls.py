"""
URLs for task_logs endpoints.
"""
from django.urls import path

from task_logs import views


app_name = "task_logs"


urlpatterns = [
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('', views.TaskListView.as_view(), name='task_index'),
]
