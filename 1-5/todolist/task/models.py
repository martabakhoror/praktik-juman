from django.db import models

# Create your models here.
class Task (models.Model):
    nama = models.CharField(max_length=30)