"""
Task logs views.
"""
from django.views import generic

from task_logs.models import Task


class IndexView(generic.ListView):
    template_name = 'task_logs/index.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        """
        Return all tasks.
        """
        return Task.objects.all()


class DetailView(generic.DetailView):
    model = Task
    template_name = 'task_logs/detail.html'
    context_object_name = 'task_detail'
