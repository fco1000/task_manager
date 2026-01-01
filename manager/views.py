from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
# from django.views.generic.edit import DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


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
    return render(request, 'form.html', {'form':form})

def taskUpdateView(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')            
    return render(request, 'form.html', {'form':form})

class WorkersView(View):
    def get(self, request):
        workers = Worker.objects.all()
        return render(request, 'workers.html', {'workers': workers})

class WorkerCreateView(View):
    def get(self, request):
        form = WorkerForm()
        return render(request, 'form.html', {'form':form})
    
    def post(self, request):
        # this is meant to handle the update
        if request.method == 'POST':
            form = WorkerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('workers')
            return render(request, 'form.html', {'form':form})
       
class WorkerUpdateView(UpdateView):
    model = Worker
    fields = ['name', 'email']
    template_name = 'form.html'
    success_url = reverse_lazy('workers')

    def get_object(self, queryset=None):
        item_id = self.kwargs.get('pk')
        return get_object_or_404(Worker, id=item_id)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        item_form = form.instance
        return self.render_to_response(self.get_context_data(form=form, item_form=item_form))
