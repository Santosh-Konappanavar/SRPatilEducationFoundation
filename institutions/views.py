from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Department, Course
from .forms import DepartmentForm, CourseForm


@login_required
def department_list(request):

    departments = Department.objects.all().order_by(
        "institution",
        "name"
    )

    return render(
        request,
        "institutions/department_list.html",
        {
            "departments": departments
        }
    )


@login_required
def department_create(request):

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("department_list")

    else:

        form = DepartmentForm()

    return render(
        request,
        "institutions/department_form.html",
        {
            "form": form
        }
    )
    @login_required
def course_list(request):

    courses = Course.objects.select_related(
        "department",
        "department__institution"
    ).order_by(
        "department__institution",
        "department",
        "name"
    )

    return render(
        request,
        "institutions/course_list.html",
        {
            "courses": courses
        }
    )


@login_required
def course_create(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:

        form = CourseForm()

    return render(
        request,
        "institutions/course_form.html",
        {
            "form": form
        }
    )