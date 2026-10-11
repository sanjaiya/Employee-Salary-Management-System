from django.contrib import admin
from .models import Department, Employee, Salary, Leave


admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Leave)