from django.http import JsonResponse
import json
from products.models import Product

# define functional based view
def api_home(request, *args, **kwargs):
    # get one random Product from the database
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)
