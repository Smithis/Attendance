from django.urls import path
from .views import home,main,apid,AdsVIew

urlpatterns = [
    path('',home),
    path('main',main),
    path('api/<str:roll>',apid),
    path('ads.txt',AdsVIew)
]
