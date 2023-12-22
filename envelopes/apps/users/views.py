from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
def index(request):
	return render(request, "users/home.html")

def reg(request):
	context = {
		'form':RegisterForm(),
	}
	return render(request, "users/register.html", context)

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect("home")
		else:
			return redirect("login")
	else:
		return render(request, "users/login.html")

def logout_user(request):
	logout(request)
	return redirect("home")