from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  # Maps the root URL to the home view
]
