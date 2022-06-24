
from django.contrib import admin
from sys_admin.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'identifier', 'is_admin', 'is_staff')
    list_filter = ('is_admin','status',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'identifier',"status")}),
        ('Permissions', {'fields': ('is_admin', 'is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'identifier', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def queryset(self, request):
        return super(Employee, self).queryset(request).filter(status=True)


#admin.site.unregister(Group)
admin.site.register(Employee, EmployeeAdmin)