
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sys_admin.api.views import *
from record.api.views import *
from management.api.views import *
from legal.api.views import *


router = DefaultRouter()
# Sys Admin
#employee_list = EmployeeViewSet.as_view({'get': 'list'})
router.register('employees', EmployeeViewSet, 'employees')

# Record
router.register('resumes', ResumeViewSet, 'resumes')
router.register('experience', ExperienceViewSet, 'experience')
router.register('education', EducationViewSet, 'education')

# Management
router.register('deparments', DepartmentViewSet, 'deparments')
router.register('roles', RoleViewSet, 'roles')
router.register('reports', ReportViewSet, 'reports')
router.register('teams', TeamViewSet, 'teams')

# Legal
router.register('salaries', SalaryViewSet, 'salaries')
router.register('vacation', VacationViewSet, 'vacation')
router.register('social_security', SocialSecurityViewSet, 'social_security')

urlpatterns = [
    path("", include(router.urls)),
    #path("", include("sys_admin.api.urls")),
    #path("employees/", EmployeeViewSet.as_view(), name="employees")
]
