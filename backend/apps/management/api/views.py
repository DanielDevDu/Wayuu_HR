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
    