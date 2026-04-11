from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Asian Tour Agency!")

def about(request):
    return HttpResponse("We are a tour agency specializing in tours across Asia.")