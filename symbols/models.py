from django.db import models


# Create your models here.
class Symbol(models.Model):
    uid = models.CharField(max_length=36)
    company_name = models.CharField(max_length=50)
    company_description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    market_values = models.TextField(max_length=10000)
