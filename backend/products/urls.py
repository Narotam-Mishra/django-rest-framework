from django.urls import path
from . import views

# /api/products/1
urlpatterns = [
    path('', views.product_mixin_view),
    path('<int:pk>/update/', views.product_mixin_view),
    path('<int:pk>/delete/', views.product_mixin_view),
    path('<int:pk>/', views.product_mixin_view)
]