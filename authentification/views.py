from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
	template_name = "authentification/login.html"

class CustomLogoutView(LogoutView):
	next_page = "/"

def signup_view(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("home")  # À adapter selon ta page d'accueil
	else:
		form = SignupForm()
	return render(request, "authentification/signup.html", {"form": form})
