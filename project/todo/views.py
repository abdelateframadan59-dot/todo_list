from django.shortcuts import render,redirect
from .forms import TaskForm
from .forms import Task
# Create your views here.



def index(request):
    tasks=Task.objects.all()
    form=TaskForm()
    if request.method == 'POST':
       form = TaskForm(request.POST)
       if  form.is_valid():     
            form.save()
            return redirect('/')

    
    return render(request,'todo/tasks.html',{'taskform':form,'tasks':tasks})


def Updatetask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method == 'POST':
           form = TaskForm(request.POST,instance=task)
           if  form.is_valid():     
                form.save()
                return redirect('/')
    return render(request,'todo/update-task.html',{'taskform':form})


def deletetask(request,pk):
     task=Task.objects.get(id=pk)
     if request.method == 'POST':
          task.delete()
          return redirect('/')
     return render(request,'todo/delete.html',{'taskk':task})
          













