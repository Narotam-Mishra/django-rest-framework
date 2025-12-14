from django.http import JsonResponse
import json

# define functional based view
def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request)

    # get url query params
    print("query params:",request.GET)

    # byte string of JSON data
    body_data = request.body  
    data = {}
    try:
        # string of JSON data --> Python's Dictionary
        data = json.loads(body_data)
    except:
        pass
    print("body data:",data)
    # print("Request header:",request.headers)

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
    # return JsonResponse({
    #     "message": "Hi there, this is Django API response!!"
    # })