from django.contrib import admin
from .models import Institution, Department, Course, AcademicYear


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "short_name",
        "code",
        "phone",
        "email",
        "is_active",
    )

    search_fields = (
        "name",
        "short_name",
        "code",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        "institution",
        "name",
        "code",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "institution",
        "is_active",
    )

    ordering = (
        "institution",
        "name",
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "department",
        "name",
        "code",
        "duration_years",
        "internship_months",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "department",
        "is_active",
    )

    ordering = (
        "department",
        "name",
    )


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):

    list_display = (
        "year",
        "start_date",
        "end_date",
        "is_current",
    )

    list_filter = (
        "is_current",
    )

    search_fields = (
        "year",
    )

    ordering = (
        "-year",
    )