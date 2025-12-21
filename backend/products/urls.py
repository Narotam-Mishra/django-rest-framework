from django.urls import path
from . import views

# /api/products/1
urlpatterns = [
    path('', views.product_create_view),
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
]