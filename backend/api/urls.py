from django.urls import path, include
from . import views

# explicit import
# from .views import api_home

urlpatterns = [
    path('', views.api_home),
    # path('products/', include('products.urls'))
]