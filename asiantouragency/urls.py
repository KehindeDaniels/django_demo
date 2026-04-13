from django.urls import path
from . import views

# define a list of url patterns for the asiantouragency app
urlpatterns = [
    path('', views.index, name='tours/index'),
    path('about/', views.about, name='tours/about'),
]