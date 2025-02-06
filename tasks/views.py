from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm 
from tasks.models import Employee, Task,TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Sum, Avg, Max, Min, F, Value, CharField
from django.contrib import messages

# Create your views here.

    # Work with database
    # Transform Data 
    # Data pass 
    # Http response or Json response or jekono dhoroner response 
    


def manager_dashboard(request):
    type = request.GET.get('type', 'all')
    
    

    # getting task count
    # total_task = Task.objects.all().count()
    # total_task = tasks.count()
    # completed_task = Task.objects.filter(status='COMPLETED').count()
    # in_progress_task = Task.objects.filter(status='IN_PROGRESS').count()
    # pending_task = Task.objects.filter(status='PENDING').count()

    counts = Task.objects.aggregate(
        total = Count('id'),
        completed = Count('id',filter=Q(status='COMPLETED')),
        in_progress = Count('id',filter=Q(status='IN_PROGRESS')),
        pending = Count('id',filter=Q(status='PENDING'))
    )

    # retriving data from database

    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
    if type == 'completed':
        tasks = base_query.filter(status='COMPLETED')
    elif type == 'in_progress':
        tasks = base_query.filter(status='IN_PROGRESS')
    elif type == 'pending':
        tasks = base_query.filter(status='PENDING')
    else:
        tasks = base_query.all()
        
    
    context = {
        'tasks': tasks,
        'counts': counts,
    } 
    return render(request, 'dashboard/manager-dashboard.html', context)


def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def test(request):
    context = {
        "names": ["Rahim", "Karim", "Rahima", "Karima", "liton"],
        "age": [20, 25, 30, 35],
    }
    return render(request, 'test.html', context)


def create_task(request):
    
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()
    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_detail_form.is_valid():
            """For Django Model Form Data"""
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Created Successfully")
            return redirect('create-task')

            

            
    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "task_form.html", context)


def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)

    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)
    
    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(request.POST, instance=task.details)

        if task_form.is_valid() and task_detail_form.is_valid():
            """For Django Model Form Data"""
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task updated Successfully")
            return redirect('update-task', id=id)

            

            
    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "task_form.html", context)


def delete_task(request,id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task Deleted Successfully")
        return redirect('manager-dashboard')
    
    else:
        messages.error(request, "Something went wrong")
        return redirect('manager-dashboard')


def view_task(request):
    # task_count = Task.objects.aggregate(num_task=Count('id'))
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')

    return render(request, "show_task.html", {"projects": projects})