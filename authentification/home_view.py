from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    form = AuthenticationForm()
    return render(request, "home.html", {"form": form})
