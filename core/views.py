from django.shortcuts import render
from django.contrib.auth.models import User
from user_auth.models import Person


# Create your views here.
def index(request):
    return render(request, "core/index.html")

def home(request):
    return render(request, "core/home.html")