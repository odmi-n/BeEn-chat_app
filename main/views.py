from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render

from .forms import LoginForm, SignUpForm


def index(request):
    return render(request, "main/index.html")


def signup(request):
    if request.method == "GET":
        form = SignUpForm()
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
            return redirect("index")
    context = {"form": form}
    return render(request, "main/signup.html", context)


class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = "main/login.html"


def friends(request):
    return render(request, "main/friends.html")