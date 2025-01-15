from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # Work with database
    # Transform Data 
    # Data pass 
    # Http response or Json response or jekono dhoroner response 
    return HttpResponse('Welcome to the task management system')


def show_task(request):
    return HttpResponse('This is Our Task page')