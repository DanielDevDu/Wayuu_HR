from django.contrib import admin

from apps.legal.models import *
# Register your models here.

admin.site.register([
    Salary,
    Vacation,
    SocialSecurity,
])