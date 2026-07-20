from django.db import models
from django.contrib.auth.models import User
from institutions.models import Institution


class UserProfile(models.Model):

    ROLE_CHOICES = [
        ("Chairman", "Chairman"),
        ("Administrator", "Administrator"),
        ("Principal", "Principal"),
        ("Accountant", "Accountant"),
        ("Office Staff", "Office Staff"),
        ("Faculty", "Faculty"),
        ("Librarian", "Librarian"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES
    )

    mobile = models.CharField(
        max_length=15,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"