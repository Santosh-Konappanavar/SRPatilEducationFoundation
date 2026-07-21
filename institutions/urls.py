from django.urls import path
from . import views

urlpatterns = [

    path(
        "departments/",
        views.department_list,
        name="department_list"
    ),

    path(
        "departments/new/",
        views.department_create,
        name="department_create"
    ),
    path(
    "courses/",
    views.course_list,
    name="course_list"
),

path(
    "courses/new/",
    views.course_create,
    name="course_create"
),

]