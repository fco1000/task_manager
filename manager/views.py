from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def taskView(request):
    tasks = Task.objects.all()

    return render(request, 'tasks.html',{'tasks':tasks})

def taskCreateView(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')            
    return render(request, 'task_create.html', {'form':form})

def taskUpdateView(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')            
    return render(request, 'task_update.html', {'form':form})

