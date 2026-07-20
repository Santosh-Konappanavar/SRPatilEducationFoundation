from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "admission_no",
        "first_name",
        "last_name",
        "mobile",
        "status",
    )

    search_fields = (
        "admission_no",
        "first_name",
        "last_name",
        "mobile",
    )

    list_filter = (
        "status",
        "gender",
    )