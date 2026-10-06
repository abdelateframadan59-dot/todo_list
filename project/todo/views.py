from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})


@login_required
def index(request):

    tasks = Task.objects.filter(user=request.user)


    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='completed').count()
    pending_tasks = tasks.filter(status='pending').count()
    in_progress_tasks = tasks.filter(status='in_progress').count()
    high_priority_tasks = tasks.filter(priority='high').count()

    search_query = request.GET.get('search', '')
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    status_filter = request.GET.get('status', '')
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    priority_filter = request.GET.get('priority', '')
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

 
    sort_by = request.GET.get('sort', '')
    if sort_by == 'due_date':
        tasks = tasks.order_by('due_date')
    elif sort_by == 'priority':
        tasks = tasks.order_by('-priority')
    elif sort_by == 'created':
        tasks = tasks.order_by('-created')

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  
            task.save()
            return redirect('index')

    context = {
        'taskform': form,
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'high_priority_tasks': high_priority_tasks,
        'search_query': search_query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'sort_by': sort_by,
    }
    return render(request, 'todo/tasks.html', context)

@login_required
def Updatetask(request, pk):

    task = get_object_or_404(Task, id=pk, user=request.user)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'todo/update-task.html', {'taskform': form, 'task': task})

@login_required
def deletetask(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'todo/delete.html', {'taskk': task})