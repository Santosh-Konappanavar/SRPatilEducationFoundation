from django import forms
from .models import Student, StudentParent, StudentAcademic


class BootstrapFormMixin:
    """
    Automatically add Bootstrap classes to all form fields.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            if isinstance(field.widget, forms.Select):
                css_class = "form-select"

            elif isinstance(field.widget, forms.CheckboxInput):
                css_class = "form-check-input"

            else:
                css_class = "form-control"

            field.widget.attrs["class"] = css_class

            field.widget.attrs.setdefault(
                "placeholder",
                field.label
            )


class StudentForm(BootstrapFormMixin, forms.ModelForm):

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
        ]

        widgets = {
            "dob": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }


class StudentParentForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = StudentParent

        fields = [
            "father_name",
            "father_mobile",
            "father_occupation",
            "father_income",
            "mother_name",
            "mother_mobile",
            "mother_occupation",
            "guardian_name",
            "guardian_mobile",
            "relationship",
        ]


class StudentAcademicForm(BootstrapFormMixin, forms.ModelForm):

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
                attrs={
                    "type": "date"
                }
            ),
        }