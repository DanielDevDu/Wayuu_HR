from legal.models import *
from rest_framework import viewsets, permissions
from legal.api.serializers import *

# Lead Viewset


class SalaryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = SalarySerializer
    queryset = Salary.objects.all()

class VacationViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = VacationSerializer
    queryset = Vacation.objects.all()

class SocialSecurityViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = SocialSecuritySerializer
    queryset = SocialSecurity.objects.all()
    