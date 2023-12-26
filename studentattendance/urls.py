from django.urls import path
from .views import home,main

urlpatterns = [
    path('',home),
    path('main',main)
]
