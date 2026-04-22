from django.urls import path
from . import views

# define a list of url patterns for the asiantouragency app
urlpatterns = [
    path('', views.tours, name='tours'),
    path('about/', views.about, name='tours/about'),
    
]
