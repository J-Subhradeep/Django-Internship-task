from django.shortcuts import render
from rest_framework import views
from ..models import Properties
from ..serializers import PropertiesSerializer
from rest_framework.response import Response
# Create your views here.

# API to add new property details
'''
 create_new_property
	Input: property name, address, city, and state.
	Output: list of properties with all details.
'''


class Create_Property(views.APIView):
    def post(self, request, format=None, *args, **kwargs):
        # serializing data received from client
        serializer = PropertiesSerializer(data=request.data)
        if (serializer.is_valid()):  # checking if the data is matching with database schema
            serializer.save()  # saving data
        else:
            return Response(serializer.errors)

         # fetching and serializing and sending response of all property details
        data = PropertiesSerializer(Properties.objects.all(), many=True)
        return Response(data.data)
