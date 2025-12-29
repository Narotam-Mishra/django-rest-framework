from rest_framework.routers import DefaultRouter
from products.viewsets import ProductGenericViewSet, ProductViewSet

router = DefaultRouter()
router.register('products-abc', ProductGenericViewSet, basename='products')

# print("Router URLs:", router.urls)
urlpatterns = router.urls

