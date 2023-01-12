# from django.shortcuts import render
# from rest_framework import views
# from ..models import Properties
# from ..serializers import PropertiesSerializer
# from rest_framework.response import Response
# # Create your views here.


# class Create_Property(views.APIView):
#     def post(self, request, format=None, *args, **kwargs):

#         serializer = PropertiesSerializer(data=request.data)
#         if (serializer.is_valid()):
#             serializer.save()
#         else:
#             return Response(serializer.errors)
#         data = PropertiesSerializer(Properties.objects.all(), many=True)
#         return Response(data.data)
