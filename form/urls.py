from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.home, name='home'),
    path('form/contact_us/', views.contact_form, name='contact_us'),
    path('form/thank_you', views.thank_you, name='thank_you')
]