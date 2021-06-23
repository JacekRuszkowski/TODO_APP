from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Task, Board
from django.views.generic import CreateView, DeleteView
from .forms import TaskForm, BoardForm

# Create your views here.


def home_view(request):
    return render(request, 'todo/home.html')


@login_required
def tasks_view(request):
    boards = Board.objects.filter(board_user=request.user)
    tasks = Task.objects.all().order_by('-id')
    user = get_object_or_404(User, username=request.user.username)
    context = {
        'boards': boards,
        'tasks': tasks,
        'user': user,
    }
    return render(request, 'todo/tasks-view.html', context)


class AddBoard(CreateView):
    form_class = BoardForm
    template_name = 'todo/board_form.html'

    def form_valid(self, form):
        form.instance.board_user = User.objects.get(username=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks-view')


def add_task(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.task_board = board
            instance.save()
        return redirect('tasks-view')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})


@login_required
def task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.task_board.board_user == request.user:
        if task.done == False:
            task.done = True
        else:
            task.done = False
        task.save()
        return redirect('tasks-view')
    else:
        return redirect('tasks-view')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.task_board.board_user == request.user:
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('tasks-view')
        else:
            form = TaskForm(instance=task)
        return render(request, 'todo/task_form.html', {'form': form})
    else:
        return redirect('tasks-view')


def edit_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if board.board_user == request.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid:
                form.save()
                return redirect('tasks-view')
        else:
            form = BoardForm(instance=board)
        return render(request, 'todo/board_form.html', {'form': form})
    else:
        return redirect('tasks-view')


class DeleteBoard(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/login/'
    model = Board

    def get_succes_url(self):
        return reverse('tasks-view')

    # sprawdzanie czy użytkownik jest twórcą tablicy i może ją edytować/usunąć
    def test_func(self):
        board = self.get_object()
        if self.request.user == board.board_user:
            return True
        else:
            return False


class DeleteTask(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/login/'
    model = Task

    def get_success_url(self):
        return reverse('tasks-view')

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.task_board.board_user:
            return True
        else:
            return False
