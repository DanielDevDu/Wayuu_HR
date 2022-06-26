from django.contrib import admin

from apps.record.models import *
# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ["id", "employee", "city", "country", "gender", "description"]
    list_filter = ["gender", "country", "city"]
    list_display_links = ["id", "employee"]

admin.site.register(Resume, ResumeAdmin)
admin.site.register([
    Education,
    Experience
])