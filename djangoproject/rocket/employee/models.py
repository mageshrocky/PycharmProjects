from uuid import uuid4

from django.db import models
# Create your models here.



class Employee(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    job = models.CharField(max_length=225)
    current_date = models.DateTimeField()

    def __str__(self):
        return self.name