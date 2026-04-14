from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from .models import Task
from .forms import SignUpForm, TaskForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}! Your account has been created.')
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    # Filter by status
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    search_query = request.GET.get('q', '')

    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    # Stats
    all_tasks = Task.objects.filter(user=request.user)
    stats = {
        'total': all_tasks.count(),
        'pending': all_tasks.filter(status='pending').count(),
        'in_progress': all_tasks.filter(status='in_progress').count(),
        'completed': all_tasks.filter(status='completed').count(),
    }

    context = {
        'tasks': tasks,
        'stats': stats,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'search_query': search_query,
    }
    return render(request, 'tasks/dashboard.html', context)


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Edit', 'task': task})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('dashboard')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if task.status == 'completed':
        task.status = 'pending'
    else:
        task.status = 'completed'
    task.save()
    return redirect('dashboard')
