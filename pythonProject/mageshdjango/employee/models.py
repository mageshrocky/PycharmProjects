from uuid import uuid4

import required as required
from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=225, blank=True)
    email = models.EmailField(max_length=225)
    job = models.CharField(max_length=225)
    current_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Employeeforms(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    mob_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    job = models.CharField(max_length=30)

    def __str__(self):
        return self.name
