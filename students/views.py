from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import (
    StudentForm,
    StudentParentForm,
    StudentAcademicForm,
)
from .models import Student
from .services import generate_admission_number
from users.models import UserProfile


@login_required
def student_list(request):

    profile = UserProfile.objects.get(user=request.user)

    if profile.role == "Administrator":
        students = Student.objects.all().order_by("admission_no")
    else:
        students = Student.objects.filter(
            institution=profile.institution
        ).order_by("admission_no")

    return render(
        request,
        "students/student_list.html",
        {
            "students": students
        }
    )


@login_required
def student_create(request):

    profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            student = form.save(commit=False)

            student.institution = profile.institution

            student.admission_no = generate_admission_number(
                profile.institution
            )

            student.save()

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {
            "form": form
        }
    )


@login_required
def admission_dashboard(request):

    profile = UserProfile.objects.get(user=request.user)

    if profile.role == "Administrator":
        students = Student.objects.all().order_by("-id")
    else:
        students = Student.objects.filter(
            institution=profile.institution
        ).order_by("-id")

    context = {
        "total_students": students.count(),
        "new_admissions": students.filter(status="Admitted").count(),
        "active_students": students.filter(status="Active").count(),
        "pending_students": students.filter(status="Applicant").count(),
        "students": students[:10],
    }

    return render(
        request,
        "students/admission_dashboard.html",
        context,
    )

@login_required
def admission_create(request):

    profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":

        student_form = StudentForm(request.POST)
        parent_form = StudentParentForm(request.POST)
        academic_form = StudentAcademicForm(request.POST)

        if (
            student_form.is_valid()
            and parent_form.is_valid()
            and academic_form.is_valid()
        ):

            with transaction.atomic():

                student = student_form.save(commit=False)

                student.institution = profile.institution
                student.admission_no = generate_admission_number(
                    profile.institution
                )
                student.status = "Admitted"
                student.save()

                parent = parent_form.save(commit=False)
                parent.student = student
                parent.save()

                academic = academic_form.save(commit=False)
                academic.student = student
                academic.save()

            return redirect(
    "student_profile",
    pk=student.pk,
)

    else:

        student_form = StudentForm()
        parent_form = StudentParentForm()
        academic_form = StudentAcademicForm()

    return render(
        request,
        "students/admission_form.html",
        {
            "student_form": student_form,
            "parent_form": parent_form,
            "academic_form": academic_form,
        },
    )

@login_required
def student_profile(request, pk):

    profile = UserProfile.objects.get(user=request.user)

    if profile.role == "Administrator":

        student = Student.objects.get(pk=pk)

    else:

        student = Student.objects.get(
            pk=pk,
            institution=profile.institution
        )

    context = {
        "student": student,
        "parent": getattr(student, "parent", None),
        "academic": getattr(student, "academic", None),
    }

    return render(
        request,
        "students/student_profile.html",
        context,
    )