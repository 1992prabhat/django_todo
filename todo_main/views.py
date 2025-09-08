from django.shortcuts import render

from todos.models import Task

def home(request):
    active_tasks = Task.objects.filter(is_completed=False).order_by('-id')

    completed_tasks = Task.objects.filter(is_completed=True).order_by('-completed_on')

    context = {
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)