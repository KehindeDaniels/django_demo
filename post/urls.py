from django.urls import path
from .views import post_list, post_page

urlpatterns = [
    path("", post_list, name="post"),
    path("<slug:slug>", post_page, name="page"),
]