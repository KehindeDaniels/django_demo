from django.shortcuts import render
from .models import Tour

def index(request):
    asian_tours = Tour.objects.all()
    return render(request, 'tours/index.html', {'asian_tours': asian_tours})

def about(request):
    print("About page accessed")
    return render(request, 'tours/about.html')