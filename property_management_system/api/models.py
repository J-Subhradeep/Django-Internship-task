from django.db import models
from django.contrib.postgres.indexes import BTreeIndex
# Create your models here.


class Properties(models.Model):
    property_name = models.CharField(max_length=200)
    address = models.CharField(max_length=600)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        # database indexing
        indexes = [BTreeIndex(
            fields=("id", "property_name", "address", "city", "state"), fillfactor=30)]
