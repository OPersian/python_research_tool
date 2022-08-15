from django.shortcuts import render
from django.views import generic

# Create your views here.


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
    template_name = 'task_logs/detail.html'
    context_object_name = 'task_detail'
