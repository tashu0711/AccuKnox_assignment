from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .rectangle import Rectangle

def rectangle_view(request):
    # Create a Rectangle instance
    rect = Rectangle((10, 5), (15, 7), (20, 10))
    
    
    # Collect iteration results
    output = []
    for item in rect:
        output.append(str(item))
    
    # Create a response
    response = "<br>".join(output)
    return HttpResponse(response)
