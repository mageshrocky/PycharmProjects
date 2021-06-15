from uuid import uuid4

from django.db import models


# Create your models here.
class Field(models.Model):
    STATUS = [
        ('pending', 'pending'),
        ('completed', 'completed'),
    ]
    id = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=30, primary_key=True)
    role = models.CharField(max_length=30)
    task = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self):
        return self.name
