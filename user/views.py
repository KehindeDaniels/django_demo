from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def register_user(request):
    return render(request, 'register.html')
    
class RegisterUser(TemplateView):
    template_name= "register.html"