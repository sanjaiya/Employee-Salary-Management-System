from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return self.name


class Salary(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    allowances = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    salary_month = models.CharField(max_length=20)
    paid_date = models.DateField()
    status = models.CharField(max_length=20, default="Paid")

    def __str__(self):
        return f"{self.employee.name} - {self.salary_month}"


class Leave(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"