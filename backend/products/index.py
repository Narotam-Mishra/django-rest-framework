from algoliasearch_django import AlgoliaIndex
from .models import Product
from algoliasearch_django.decorators import register

@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'title',
        'body',
        'price',
        'user_id',
        'public',
        'path',
    ]
    settings = {
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['user', 'public']
    }

    tags = 'get_tags_list'

    def get_user_id(self, instance):
        """Custom method to safely get user ID"""
        return instance.user.id if instance.user else None


# admin.site.register(Product, ProductModelAdmin)