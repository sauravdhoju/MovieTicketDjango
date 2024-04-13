from django.shortcuts import render
from django.utils import timezone
from django.render import render, redirect
# Create your views here.
def index(request):
    return render(request, 'home.html')

