from django.urls import path
from home.views import index, home

urlpatterns = [
    path('', index, name="index"),
    path('', home, name="home"),
]