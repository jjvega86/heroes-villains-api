from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def api_overview(request):
    routes = {
        "api": {
            "GET api overview": "/"
        },
        "supers": {
            "GET all supers": "/api/supers",
            "GET super by id": "/api/supers/<int:pk>",
            "POST a new super": "/api/supers"
        }
    }
    return Response(data=routes, template_name=None)
