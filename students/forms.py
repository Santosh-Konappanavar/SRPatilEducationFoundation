from django import forms
from .models import Student,StudentAcademic


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
class StudentAcademicForm(forms.ModelForm):

    class Meta:
        model = StudentAcademic

        fields = [
            "department",
            "course",
            "academic_year",
            "semester",
            "batch",
            "roll_number",
            "admission_date",
        ]

        widgets = {
            "admission_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }