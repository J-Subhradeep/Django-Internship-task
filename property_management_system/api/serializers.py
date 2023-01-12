from rest_framework.serializers import ModelSerializer
from .models import Properties


class PropertiesSerializer(ModelSerializer):
    class Meta:
        model = Properties
        fields = "__all__"
