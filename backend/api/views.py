import json
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict

# define functional based view
def api_home(request, *args, **kwargs):
    # get one random Product from the database
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)    
    #     print("Model Data:", data)
    #     # convert dictionary into json response
    #     json_data = json.dumps(data)
    # return HttpResponse(json_data, headers={"content-type": "application/json"})
