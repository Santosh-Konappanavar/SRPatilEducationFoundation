from django.contrib import admin
from .models import Department, Course, AcademicYear


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "institution", "is_active")
    search_fields = ("name", "code")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "department",
        "institution",
        "duration_years",
        "internship_months",
        "is_active",
    )


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "start_date",
        "end_date",
        "is_current",
    )