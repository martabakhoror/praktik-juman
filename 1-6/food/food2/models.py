from django.db import models
from django.db.models.expressions import Value

# Create your models here.


class Task(models.Model):
    makanan = models.TextField(default='', blank=True, null=True)
    jenismakanan = models.CharField(max_length=20)
    hargamakanan = models.IntegerField(blank=True, null=True)
    minuman = models.TextField(default='', blank=True, null=True)
    hargaminuman = models.IntegerField(blank=True, null=True)


# foreign key =
