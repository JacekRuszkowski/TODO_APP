from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from users.forms import RegistrationForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.add_message(request, messages.INFO,
                             f'Konto utworzone. Zaloguj się.')
        return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tasks-view')
        else:
            messages.add_message(request, messages.INFO,
                                 f'Nazwa użytkonika lub hasło są niepoprawne.')
            return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
