from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           print(form.cleaned_data)
           request.session['form_data'] = form.cleaned_data
           return redirect('thank_you')
    else :
        form = ContactForm()
        return render(request, 'contact.html', {'form':form})

def thank_you(request):
    data = request.session.get('form_data')
    return render(request, 'thank-you.html', {'data':data})