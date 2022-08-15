"""
Task logs views.
"""
from django.views import generic

from task_logs.models import Task


class TaskListView(generic.ListView):
    template_name = 'task_logs/list.html'
    context_object_name = 'tasks_list'
    # TODO pagination

    def get_queryset(self):
        """
        Return all tasks.
        """
        return Task.objects.all()


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task_logs/detail.html'
    context_object_name = 'task_detail'


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'task_logs/create.html'
    context_object_name = 'task_create'  # TODO needed?
    # TODO introduce form
    # TODO FIXME ImproperlyConfigured at /tasks/create/
