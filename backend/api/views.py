from django.http import JsonResponse

# define functional based view
def api_home(request, *args, **kwargs):
    return JsonResponse({
        "message": "Hi there, this is Django API response!!"
    })