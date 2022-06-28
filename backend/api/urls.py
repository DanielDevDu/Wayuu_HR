
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.sys_admin.api.views import *
from apps.record.api.views import *
from apps.management.api.views import *
from apps.legal.api.views import *


router = DefaultRouter()
# Sys Admin
#employee_list = EmployeeViewSet.as_view({'get': 'list'})
router.register('employee', EmployeeViewSet, basename='employee')

# Record
router.register('resume', ResumeViewSet, basename='resume')
router.register('experience', ExperienceViewSet, basename='experience')
router.register('education', EducationViewSet, basename='education')

# Management
router.register('department', DepartmentViewSet, 'department')
router.register('role', RoleViewSet, 'role')
router.register('report', ReportViewSet, 'report')
router.register('team', TeamViewSet, 'team')

# Legal
router.register('salary', SalaryViewSet, 'salary')
router.register('vacation', VacationViewSet, 'vacation')
router.register('socialsecurity', SocialSecurityViewSet, 'socialsecurity')

urlpatterns = [
    path("", include(router.urls)),
    #path("", include("sys_admin.api.urls")),
    #path("employees/", EmployeeViewSet.as_view(), name="employees")
]
