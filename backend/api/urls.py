from django.urls import path
from . import views

# explicit import
# from .views import api_home

urlpatterns = [
    path('', views.api_home)
]