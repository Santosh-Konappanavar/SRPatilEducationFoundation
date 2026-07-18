from django.db import models
from core.models import BaseModel
from institutions.models import Institution


class Department(BaseModel):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(BaseModel):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    duration_years = models.PositiveIntegerField()

    internship_months = models.PositiveIntegerField(default=6)

    def __str__(self):
        return self.name


class AcademicYear(BaseModel):
    year = models.CharField(max_length=20)

    start_date = models.DateField()

    end_date = models.DateField()

    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.year