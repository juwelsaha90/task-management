from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task

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
    # employees = Employee.objects.all()
    form = TaskModelForm()
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """For Django Model Form Data"""
            form.save()

            return render(request, 'task_form.html', {"form": form, "message": "Task Added Successfully"})

            '''For Django Form Data'''
            # data = form.cleaned_data
            # title = data.get("title")
            # description = data.get("description")
            # due_date = data.get("due_date")
            # assigned_to = data.get("assigned_to")

            # task = Task.objects.create(
            #     title = title,
            #     description = description,
            #     due_date = due_date,
            # )
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)
            # return HttpResponse("Task Created Successfully")

            
    context = {"form": form}
    return render(request, "task_form.html", context)

def view_task(request):
    # retrive all data from tasks model
    task = Task.objects.all()

    # retrive single data from tasks model

    task_3 = Task.objects.get(id=1)
    return render(request, "show_task.html", {"tasks": task, "task3": task_3})