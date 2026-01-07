from algoliasearch_django import AlgoliaIndex
from .models import Product
from algoliasearch_django.decorators import register

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        'title',
        'content',
        'price',
        'user_id',
        'public',
    ]

    def get_user_id(self, instance):
        """Custom method to safely get user ID"""
        return instance.user.id if instance.user else None


# admin.site.register(Product, ProductModelAdmin)