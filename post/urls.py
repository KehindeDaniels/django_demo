from django.urls import path
from .views import post_list, post_page

app_name = 'post'
urlpatterns = [
    path("", post_list, name="list"),
    path("<slug:slug>", post_page, name="page"),
]