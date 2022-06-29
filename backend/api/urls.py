
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.sys_admin.api.views import *
from apps.record.api.views import *
from apps.management.api.views import *
from apps.legal.api.views import *
from django.contrib.auth import urls
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()
# Sys Admin
#employee_list = EmployeeViewSet.as_view({'get': 'list'})
router.register('employee', EmployeeViewSet, basename='employee')
#router.register('login', LoginViewSet, basename='login')
#router.register('auth', urls.urlpatterns , basename='auth')
employee_detail = EmployeeViewSet.as_view({
    'get': 'employee_active'
})

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

urls= format_suffix_patterns([
    #path('', include('rest_framework.urls', namespace='rest_framework'))
    #path('auth/', include('django.contrib.auth.urls')),

    #path("employees/", EmployeeViewSet.as_view(), name="employees")
])

urlpatterns = router.urls + urls
