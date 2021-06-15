from uuid import uuid4

from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    mob_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.name
