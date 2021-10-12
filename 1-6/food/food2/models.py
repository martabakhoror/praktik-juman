from django.db import models

# Create your models here.


class Task(models.Model):
    item = models.TextField(default='')
    harga = models.IntegerField()
