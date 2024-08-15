from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SearchParams(models.Model):
    destination = models.CharField(max_length=100)
    adults = models.IntegerField()
    children = models.IntegerField()
    infants = models.IntegerField()

    class Meta:
        unique_together = ['destination', 'adults', 'children', 'infants']



class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_params = models.ForeignKey(SearchParams, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    

class History(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)