from django.contrib import admin

from legal.models import *
# Register your models here.

admin.site.register([
    Salary,
    Vacation,
    SocialSecurity,
    Employee_Salary,
])