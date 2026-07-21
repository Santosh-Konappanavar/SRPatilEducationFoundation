from django.db import models
from core.models import BaseModel
from institutions.models import Department, Course, AcademicYear, Institution


class Student(BaseModel):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    ADMISSION_TYPE = [
        ('PUC', 'PUC'),
        ('Diploma', 'Diploma Lateral Entry'),
    ]

    STATUS_CHOICES = [
        ('Applicant', 'Applicant'),
        ('Admitted', 'Admitted'),
        ('Active', 'Active'),
        ('Internship', 'Internship'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
        ('Transfer', 'Transfer'),
        ('Alumni', 'Alumni'),
    ]

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE
    )

    admission_no = models.CharField(
        max_length=30,
        unique=True
    )

    first_name = models.CharField(max_length=100)

    middle_name = models.CharField(
        max_length=100,
        blank=True
    )

    last_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    dob = models.DateField()

    mobile = models.CharField(max_length=15)

    email = models.EmailField(blank=True)

    aadhaar = models.CharField(
        max_length=20,
        blank=True
    )

    admission_type = models.CharField(
        max_length=20,
        choices=ADMISSION_TYPE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Applicant"
    )

    def __str__(self):
        return f"{self.admission_no} - {self.first_name} {self.last_name}"


class StudentParent(BaseModel):

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="parent"
    )

    father_name = models.CharField(max_length=200)

    father_mobile = models.CharField(
        max_length=15,
        blank=True
    )

    father_occupation = models.CharField(
        max_length=100,
        blank=True
    )

    father_income = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    mother_name = models.CharField(max_length=200)

    mother_mobile = models.CharField(
        max_length=15,
        blank=True
    )

    mother_occupation = models.CharField(
        max_length=100,
        blank=True
    )

    guardian_name = models.CharField(
        max_length=200,
        blank=True
    )

    guardian_mobile = models.CharField(
        max_length=15,
        blank=True
    )

    relationship = models.CharField(
        max_length=50,
        blank=True
    )

    def __str__(self):
        return f"{self.student.admission_no} - Parent"
class StudentAcademic(BaseModel):

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="academic"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT
    )

    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.PROTECT
    )

    semester = models.PositiveSmallIntegerField(default=1)

    batch = models.CharField(
        max_length=30,
        blank=True
    )

    roll_number = models.CharField(
        max_length=30,
        blank=True
    )

    admission_date = models.DateField()

    def __str__(self):
        return f"{self.student.admission_no} - Academic"