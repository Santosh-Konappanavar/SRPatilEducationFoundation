from django import forms
from .models import Department, Course


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = [
            "institution",
            "name",
            "code",
            "is_active",
        ]


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = [
            "department",
            "name",
            "code",
            "duration_years",
            "internship_months",
            "is_active",
        ]