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
            "POST a new super": "/api/supers",
            "GET super by id": "/api/supers/<int:pk>",
            "PUT an existing super": "/api/supers/<int:pk>",
            "DELETE an existing super": "/api/supers/<int:pk>",
            "GET supers by type": "/api/supers?type=<super_type.type>"
        }
    }
    return Response(data=routes, template_name=None)
