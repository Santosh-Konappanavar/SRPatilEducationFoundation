from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "dob",
            "mobile",
            "email",
            "aadhaar",
            "admission_type",
            "status",
        ]

        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
        }