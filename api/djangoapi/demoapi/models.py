from uuid import uuid4

from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=10)
    job = models.CharField(max_length=30)
    address = models.JSONField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
