from django.urls import path
from .store_info.create_property_view import Create_Property
urlpatterns = [
    path('create_property/', Create_Property.as_view(), name="create_property")

]
