from apps.management.models import *
from rest_framework import viewsets, permissions
from apps.management.api.serializers import *

# Lead Viewset


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class ReportViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    
class EmployeeRoleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = EmployeeRoleSerializer
    queryset = Employee_Role.objects.all()

class EmployeeDepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    action_serializer_classes = {
      "create": EmployeeDepartmentCreateSerializer,
      "update": EmployeeDepartmentUpdateSerializer,
      "retrieve": EmployeeDepartmentReadSerializer,
      "list": EmployeeDepartmentReadSerializer,
      "partial_update": EmployeeDepartmentUpdateSerializer,
     }
    
    def get_serializer_class(self):
        # What serializer use?
        return self.action_serializer_classes[self.action]
 
    queryset = Employee_Department.objects.all()