from django.db import models
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.title