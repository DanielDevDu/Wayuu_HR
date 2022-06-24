from django.contrib import admin

from record.models import *
# Register your models here.

admin.site.register([
    Education,
    Resume,
    Experience,
])