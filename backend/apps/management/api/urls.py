from rest_framework import routers
from management.api.views import *

router = routers.DefaultRouter()
router.register('deparments', DepartmentViewSet, 'deparments')
router.register('roles', RoleViewSet, 'roles')
router.register('reports', ReportViewSet, 'reports')
router.register('teams', TeamViewSet, 'teams')
router.register('employe_role', EmployeeRoleViewSet, 'employee_role')

urlpatterns = router.urls