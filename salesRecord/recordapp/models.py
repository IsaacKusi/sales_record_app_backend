from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class SaleItem(models.Model):
    date = models.CharField(max_length=100)
    amount = models.IntegerField()
    item_id = models.IntegerField()
    user_id = models.IntegerField()




