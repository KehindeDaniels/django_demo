from django.shortcuts import render
from .models import Tour

def tours(request):
    asian_tours = Tour.objects.all()
    return render(request, 'tours/tours.html', {'asian_tours': asian_tours})

def about(request):
    print("About page accessed")
    return render(request, 'tours/about.html')