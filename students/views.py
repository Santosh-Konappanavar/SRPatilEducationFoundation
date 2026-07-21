from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm
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