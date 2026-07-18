from django.contrib import admin
from .models import Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_name",
        "code",
        "phone",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )