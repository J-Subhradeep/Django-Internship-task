from django.shortcuts import render
from rest_framework import views
from ..models import Properties
from ..serializers import PropertiesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.
'''
update_property_details
	Input: property_id, property name, address, city, state
	Output: same as create_new_property API with updated information
'''

class Update_Property(views.APIView):
    def get_object(self, pk):
        ''' Getting record using primary key'''
        try:
            return Properties.objects.get(pk=pk)
        except Properties.DoesNotExist:
            raise Http404

    def request_data_refactor(self, data, obj):
        ''' If incomplete data is given by user against an id the method helps
        to complete the data using the 'id' and 'the provided incomplete data' '''
        serializer = PropertiesSerializer(obj)
        return {**serializer.data, **data}

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)  # getting object with id=pk
        serializer = PropertiesSerializer(
            obj, data=self.request_data_refactor(request.data, obj))
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = PropertiesSerializer(Properties.objects.all(), many=True)
        return Response(data.data)
