"""
URLs for task_logs endpoints.
"""
from django.urls import path

from task_logs import views


app_name = "task_logs"


urlpatterns = [
    path('', views.IndexView.as_view(), name='task_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='task_detail'),
]
