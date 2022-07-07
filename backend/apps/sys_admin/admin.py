
from django.contrib import admin
from apps.sys_admin.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

class EmployeeAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = Employee
    list_display = [
        "email",
        "identifier",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "username",
    ]
    list_display_links = ["email"]
    list_filter = [
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    "last_name_second",
                    "identifier",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "identifier",
                    "password1", "password2", "is_staff",
                    
                ),
            },
        ),
    )
    search_fields = ["email", "identifier", "first_name", "last_name", "username"]
    ordering = ('email',)
    #filter_horizontal = ()

    """def queryset(self, request):
        return super(Employee, self).queryset(request).filter(status=True)"""


# admin.site.unregister(Group)
admin.site.register(Employee, EmployeeAdmin)