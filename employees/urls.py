from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path(
        "employees/",
        views.employee_list,
        name="employee_list"
    ),

    path(
        "employees/add/",
        views.employee_add,
        name="employee_add"
    ),

    path(
        "employees/edit/<int:id>/",
        views.employee_edit,
        name="employee_edit"
    ),

    path(
        "employees/delete/<int:id>/",
        views.employee_delete,
        name="employee_delete"
    ),

    path(
    "salary/add/",
    views.salary_add,
    name="salary_add"
),
path(
    "salary/",
    views.salary_list,
    name="salary_list"
),
path(
    "salary/edit/<int:id>/",
    views.salary_edit,
    name="salary_edit"
),
path(
    "salary/delete/<int:id>/",
    views.salary_delete,
    name="salary_delete"
),

    path(
        "leave/",
        views.leave_list,
        name="leave_list"
    ),

    path(
        "leave/add/",
        views.leave_add,
        name="leave_add"
    ),

    path(
        "leave/edit/<int:id>/",
        views.leave_edit,
        name="leave_edit"
    ),

    path(
        "leave/delete/<int:id>/",
        views.leave_delete,
        name="leave_delete"
    ),

    path(
    "login/",
    views.login_view,
    name="login"
),

path(
    "logout/",
    views.logout_view,
    name="logout"
),

path("departments/", views.department_list, name="department_list"),
path("departments/add/", views.department_add, name="department_add"),
path("departments/edit/<int:id>/", views.department_edit, name="department_edit"),
path("departments/delete/<int:id>/", views.department_delete, name="department_delete"),

]