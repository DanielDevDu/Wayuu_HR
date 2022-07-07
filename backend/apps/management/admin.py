from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.management.models import *
# Register your models here.

class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ["employee", "role", "status", "start_date", "end_date"]
    list_filter = ["role", "status", "employee"]
    list_display_links = ["employee"]

class EmployeeDepartmentAdmin(admin.ModelAdmin):
    list_display = ["employee", "department", "status", "start_date", "end_date"]
    list_filter = ["department", "status", "employee"]
    list_display_links = ["employee"]

class EmployeeTeamAdmin(admin.ModelAdmin):
    list_display = ["employee", "team", "status", "start_date", "end_date"]
    list_filter = ["team", "status", "employee"]
    list_display_links = ["employee"]

admin.site.register(
    Employee_Role,
    EmployeeRoleAdmin)
admin.site.register(
    Employee_Department,
    EmployeeDepartmentAdmin)
admin.site.register(
    Employee_Team,
    EmployeeTeamAdmin)
admin.site.register([
    Department,
    Report,
    Role,
    Team,
    Employee_Report,
    Department_Role,
    Employee_Deparment_Role
])