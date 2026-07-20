from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "institution",
        "role",
        "mobile",
        "is_active",
    )

    list_filter = (
        "institution",
        "role",
    )

    search_fields = (
        "user__username",
        "mobile",
    )