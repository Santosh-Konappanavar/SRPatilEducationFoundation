from datetime import datetime
from .models import Student


def generate_admission_number(institution):
    """
    Generates admission number like:
    AHS-2026-0001
    """

    year = datetime.now().year

    last_student = (
        Student.objects.filter(institution=institution)
        .order_by("-id")
        .first()
    )

    if last_student and last_student.admission_no:
        try:
            last_number = int(last_student.admission_no.split("-")[-1])
        except (ValueError, IndexError):
            last_number = 0
    else:
        last_number = 0

    next_number = last_number + 1

    return f"{institution.code}-{year}-{next_number:04d}"