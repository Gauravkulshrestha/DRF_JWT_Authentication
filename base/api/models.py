from unicodedata import name
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name   