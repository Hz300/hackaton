from django.shortcuts import render
import json
from django.http import HttpResponseBadRequest
from django.http import JsonResponse

def initialize_level(request):
    request.session['level'] = 1
    return HttpResponse("Level initialized successfully")

def get_level(request):
    # Retrieve the current level from your session or database
    current_level = request.session.get('level', 0)  # Assuming the level is stored in the session

    return JsonResponse({'level': current_level})


def index(request):
    if 'level' not in request.session:
        # If not set, initialize it
        request.session['level'] = 1
    print(request.session.items())
    return render(request, "app_emprende/index.html")



# view for incrementing levelimport json
from django.http import HttpResponseBadRequest

def update_level(request):
    if request.method == 'POST':
        # Parse the JSON data from the request body
        data = json.loads(request.body)
        new_level_value = data.get('level')

        if new_level_value is not None:
            # Perform the necessary updates
            # Update the session variable 'level', for example:
            request.session['level'] = new_level_value
            return JsonResponse({'message': 'Level updated successfully'})
        else:
            # Return a bad request response if 'level' is not provided
            return HttpResponseBadRequest('Missing or invalid "level" parameter in request JSON')
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Method not allowed'}, status=405)
