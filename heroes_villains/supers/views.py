from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import SuperSerializer
from .models import Super, Power

# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):
    type_param = request.query_params.get('type')
    if type_param:
        supers = Super.objects.filter(super_type__type=type_param)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    if request.method == 'GET':
        custom_response = {
            "heroes": [],
            "villains": [],
        }
        supers = Super.objects.all()
        for super in supers:
            serializer = SuperSerializer(super)
            if super.super_type.type == "Hero":
                custom_response["heroes"].append(serializer.data)
            else:
                custom_response["villains"].append(serializer.data)
        return Response(custom_response)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    try:
        super = Super.objects.get(id=pk)
    except Super.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
def supers_super_powers(request, super_pk, power_pk):
    try:
        super = Super.objects.get(id=super_pk)
        power = Power.objects.get(id=power_pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    super.powers.add(power)
    super.save()
    serializer = SuperSerializer(super)
    return Response(serializer.data, status=status.HTTP_200_OK)
