from django.urls import path
from .store_info.create_property_view import Create_Property
from .store_info.update_property_view import Update_Property
urlpatterns = [
    path('create_property/', Create_Property.as_view(), name="create_property"),
    path('update_property/<int:pk>/',
         Update_Property.as_view(), name="update_property"),
]
