"""
--------------------------------------
Enpoints of the API with router with
rest framework, urls.
--------------------------------------
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.sys_admin.api.views import *
from apps.record.api.views import *
from apps.management.api.views import *
from apps.legal.api.views import *
from django.contrib.auth import urls
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter(trailing_slash=True)
#W## Sys Admin ###
router.register('employee', EmployeeViewSet, basename='employee')
router.register('login', LoginViewSet, basename='login')
router.register('logout', LogoutViewSet, basename='logout')

### Record ###
router.register('resume', ResumeViewSet, basename='resume')
router.register('experience', ExperienceViewSet, basename='experience')
router.register('education', EducationViewSet, basename='education')

### Management ###
router.register('department', DepartmentViewSet, 'department')
router.register('role', RoleViewSet, 'role')
router.register('report', ReportViewSet, 'report')
router.register('team', TeamViewSet, 'team')

# Intermediate tables #
router.register('employee_role', EmployeeRoleViewSet, 'employee_role')
router.register('employee_department', EmployeeDepartmentViewSet, 'employee_department')

### Legal ###
router.register('salary', SalaryViewSet, 'salary')
router.register('vacation', VacationViewSet, 'vacation')
router.register('socialsecurity', SocialSecurityViewSet, 'socialsecurity')

urls= format_suffix_patterns([])

urlpatterns = router.urls + urls
