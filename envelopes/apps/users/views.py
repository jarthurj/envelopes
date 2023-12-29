from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
def index(request):
	return render(request, "users/home.html")

def reg(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect("home")
	else:
		request.session['errors'] = None
		context = {
			'form':RegisterForm(),
		}
		return render(request, "users/register.html", context)
	return render(request, "users/register.html", {'form':form})

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