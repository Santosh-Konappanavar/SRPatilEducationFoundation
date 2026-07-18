from django.db import models
from core.models import BaseModel


class Institution(BaseModel):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)

    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name