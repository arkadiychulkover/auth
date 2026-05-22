from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponseNotAllowed, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

def register_page(request: HttpRequest):
    return render(request, "register.html", {"form": RegistrationForm()})
 
def register_view(request: HttpRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("auth_page")
        else:
            return render(request, "register.html", {"form": form})
    return HttpResponseNotAllowed(["POST"])


def login_page(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("auth_page")
    return render(request, "register.html", {"form": AuthenticationForm(), "button": "Login", "action": 'login_view'})


def login_view(request: HttpRequest):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('auth_page')
        else:
            return render(request, "register.html", {"form": form, "button": "Login", "action": 'login_view'})
    return HttpResponseNotAllowed(['POST'])


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('login_page')

#
@login_required
def auth_page(request: HttpRequest):
    return render(request, 'auth.html', {'user': request.user})


@login_required
def create_user(request: HttpRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("auth_page")
    else:
        form = RegistrationForm()
    return render(request, "base_form.html", {"form": form, "button": "Create User"})


@login_required
def create_manager(request: HttpRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect("auth_page")
    else:
        form = RegistrationForm()
    return render(request, "base_form.html", {"form": form, "button": "Create Manager"})


def test(request):
    if request.method == 'POST':
        a = 10
    else:
        print(a)