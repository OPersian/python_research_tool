"""
Main views.
"""

from django.views import generic

from task_logs.models import Task

TASKS_NUMBER_ON_INDEX_PAGE = 5


class IndexView(generic.ListView):
    template_name = 'python_research_tool/index.html'
    context_object_name = 'latest_tasks_list'

    def get_queryset(self):
        """
        Return n-latest tasks sorted in natural order. TODO ensure the sorting
        """
        if Task.objects.exists():
            # TODO consider ridding of nested if, reducing db hits number
            if Task.objects.count() >= TASKS_NUMBER_ON_INDEX_PAGE:
                return Task.objects.all()[:TASKS_NUMBER_ON_INDEX_PAGE]
            else:
                return Task.objects.all()
        else:
            return None
