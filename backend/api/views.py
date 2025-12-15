import json
# from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


# define functional based view
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """ DRF API View """
    # get one random Product from the database
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return Response(data)    
