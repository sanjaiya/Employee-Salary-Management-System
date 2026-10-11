from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Department, Employee, Salary, Leave


# =========================
# DASHBOARD
# =========================

@login_required(login_url="/login/")
def dashboard(request):

    context = {
        "department_count": Department.objects.count(),
        "employee_count": Employee.objects.count(),
        "salary_count": Salary.objects.count(),
        "leave_count": Leave.objects.count(),
    }

    return render(
        request,
        "dashboard.html",
        context
    )


# =========================
# EMPLOYEE MANAGEMENT
# =========================
# =========================
# EMPLOYEE MANAGEMENT
# =========================

def employee_list(request):

    search = request.GET.get("search", "").strip()

    if search:
        employees = Employee.objects.filter(
            name__icontains=search
        )
    else:
        employees = Employee.objects.all()

    for employee in employees:

        salary = Salary.objects.filter(
            employee=employee
        ).last()

        if salary:
            employee.current_salary = (
                salary.basic_salary
                + salary.allowances
                - salary.deductions
            )
        else:
            employee.current_salary = None

    return render(
        request,
        "employee_list.html",
        {
            "employees": employees,
            "search": search
        }
    )
def employee_add(request):

    departments = Department.objects.all()

    if request.method == "POST":

        Employee.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            age=request.POST["age"],
            department_id=request.POST["department"],
            designation=request.POST["designation"],
            joining_date=request.POST["joining_date"],
            status=request.POST["status"],
        )

        return redirect("employee_list")

    return render(
        request,
        "employee_add.html",
        {"departments": departments}
    )


def employee_edit(request, id):

    employee = Employee.objects.get(id=id)
    departments = Department.objects.all()

    if request.method == "POST":

        employee.name = request.POST["name"]
        employee.email = request.POST["email"]
        employee.phone = request.POST["phone"]
        employee.age = request.POST["age"]
        employee.department_id = request.POST["department"]
        employee.designation = request.POST["designation"]
        employee.joining_date = request.POST["joining_date"]
        employee.status = request.POST["status"]

        employee.save()

        return redirect("employee_list")

    return render(
        request,
        "employee_edit.html",
        {
            "employee": employee,
            "departments": departments
        }
    )


def employee_delete(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        employee.delete()

        return redirect("employee_list")

    return render(
        request,
        "employee_delete.html",
        {"employee": employee}
    )


# =========================
# SALARY MANAGEMENT
# =========================

def salary_add(request):

    employees = Employee.objects.all()

    if request.method == "POST":

        Salary.objects.create(
            employee_id=request.POST["employee"],
            basic_salary=request.POST["basic_salary"],
            allowances=request.POST["allowances"],
            deductions=request.POST["deductions"],
            salary_month=request.POST["salary_month"],
            paid_date=request.POST["paid_date"],
            status=request.POST["status"],
        )

        return redirect("salary_list")

    return render(
        request,
        "salary_add.html",
        {"employees": employees}
    )


def salary_list(request):

    salaries = Salary.objects.all()

    for salary in salaries:

        salary.total_salary = (
            salary.basic_salary
            + salary.allowances
            - salary.deductions
        )

    return render(
        request,
        "salary_list.html",
        {"salaries": salaries}
    )


def salary_edit(request, id):

    salary = Salary.objects.get(id=id)
    employees = Employee.objects.all()

    if request.method == "POST":

        salary.employee_id = request.POST["employee"]
        salary.basic_salary = request.POST["basic_salary"]
        salary.allowances = request.POST["allowances"]
        salary.deductions = request.POST["deductions"]
        salary.salary_month = request.POST["salary_month"]
        salary.paid_date = request.POST["paid_date"]
        salary.status = request.POST["status"]

        salary.save()

        return redirect("salary_list")

    return render(
        request,
        "salary_edit.html",
        {
            "salary": salary,
            "employees": employees
        }
    )


def salary_delete(request, id):

    salary = Salary.objects.get(id=id)

    if request.method == "POST":

        salary.delete()

        return redirect("salary_list")

    return render(
        request,
        "salary_delete.html",
        {"salary": salary}
    )


# =========================
# LEAVE MANAGEMENT
# =========================

def leave_list(request):

    leaves = Leave.objects.all().order_by("-id")

    return render(
        request,
        "leave_list.html",
        {"leaves": leaves}
    )


def leave_add(request):

    employees = Employee.objects.all()

    if request.method == "POST":

        Leave.objects.create(
            employee_id=request.POST["employee"],
            leave_type=request.POST["leave_type"],
            start_date=request.POST["start_date"],
            end_date=request.POST["end_date"],
            reason=request.POST["reason"],
            status=request.POST["status"],
        )

        return redirect("leave_list")

    return render(
        request,
        "leave_add.html",
        {"employees": employees}
    )


def leave_edit(request, id):

    leave = Leave.objects.get(id=id)
    employees = Employee.objects.all()

    if request.method == "POST":

        leave.employee_id = request.POST["employee"]
        leave.leave_type = request.POST["leave_type"]
        leave.start_date = request.POST["start_date"]
        leave.end_date = request.POST["end_date"]
        leave.reason = request.POST["reason"]
        leave.status = request.POST["status"]

        leave.save()

        return redirect("leave_list")

    return render(
        request,
        "leave_edit.html",
        {
            "leave": leave,
            "employees": employees
        }
    )


def leave_delete(request, id):

    leave = Leave.objects.get(id=id)

    if request.method == "POST":

        leave.delete()

        return redirect("leave_list")

    return render(
        request,
        "leave_delete.html",
        {"leave": leave}
    )


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        return render(
            request,
            "login.html",
            {
                "error": "Invalid username or password"
            }
        )

    return render(
        request,
        "login.html"
    )


# =========================
# LOGOUT
# =========================

def logout_view(request):

    logout(request)

    return redirect("login")


# =========================
# DEPARTMENT MANAGEMENT
# =========================

def department_list(request):

    departments = Department.objects.all().order_by("id")

    return render(
        request,
        "department_list.html",
        {
            "departments": departments
        }
    )


def department_add(request):

    if request.method == "POST":

        Department.objects.create(
            dept_name=request.POST["dept_name"]
        )

        return redirect("department_list")

    return render(
        request,
        "department_add.html"
    )


def department_edit(request, id):

    department = Department.objects.get(id=id)

    if request.method == "POST":

        department.dept_name = request.POST["dept_name"]
        department.save()

        return redirect("department_list")

    return render(
        request,
        "department_edit.html",
        {
            "department": department
        }
    )


def department_delete(request, id):

    department = Department.objects.get(id=id)

    if request.method == "POST":

        department.delete()

        return redirect("department_list")

    return render(
        request,
        "department_delete.html",
        {
            "department": department
        }
    )