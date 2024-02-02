from django.urls import path
from .views import home,main,apid

urlpatterns = [
    path('',home),
    path('main',main),
    path('api/<str:roll>',apid)
]
