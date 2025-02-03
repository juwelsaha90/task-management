from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task,TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Sum, Avg, Max, Min, F, Value, CharField

# Create your views here.

    # Work with database
    # Transform Data 
    # Data pass 
    # Http response or Json response or jekono dhoroner response 
    


def manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')


def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def test(request):
    context = {
        "names": ["Rahim", "Karim", "Rahima", "Karima", "liton"],
        "age": [20, 25, 30, 35],
    }
    return render(request, 'test.html', context)


def create_task(request):
    
    form = TaskModelForm()
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """For Django Model Form Data"""
            form.save()

            return render(request, 'task_form.html', {"form": form, "message": "Task Added Successfully"})

            

            
    context = {"form": form}
    return render(request, "task_form.html", context)

def view_task(request):
    # task_count = Task.objects.aggregate(num_task=Count('id'))
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')

    return render(request, "show_task.html", {"projects": projects})