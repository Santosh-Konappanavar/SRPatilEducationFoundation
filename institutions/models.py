from django.db import models
from core.models import BaseModel


class Institution(BaseModel):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)

    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Department(BaseModel):
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.institution.short_name} - {self.name}"


class Course(BaseModel):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20)

    duration_years = models.PositiveSmallIntegerField(default=3)
    internship_months = models.PositiveSmallIntegerField(default=6)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class AcademicYear(BaseModel):
    year = models.CharField(max_length=20)

    start_date = models.DateField()

    end_date = models.DateField()

    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.year