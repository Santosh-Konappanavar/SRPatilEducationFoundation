from django.contrib import admin
from .models import Student, StudentParent, StudentAcademic


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "admission_no",
        "first_name",
        "last_name",
        "institution",
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
        "institution",
        "status",
        "gender",
    )

    ordering = (
        "admission_no",
    )


@admin.register(StudentParent)
class StudentParentAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "father_name",
        "mother_name",
        "father_mobile",
        "mother_mobile",
    )

    search_fields = (
        "student__admission_no",
        "father_name",
        "mother_name",
    )

    ordering = (
        "student",
    )


@admin.register(StudentAcademic)
class StudentAcademicAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "department",
        "course",
        "academic_year",
        "semester",
        "roll_number",
    )

    list_filter = (
        "department",
        "course",
        "academic_year",
        "semester",
    )

    search_fields = (
        "student__admission_no",
        "student__first_name",
        "student__last_name",
        "roll_number",
    )

    ordering = (
        "student",
    )