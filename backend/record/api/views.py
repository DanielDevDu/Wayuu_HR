from record.models import *
from rest_framework import viewsets, permissions
from record.api.serializers import *

# Lead Viewset


class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = EducationSerializer
    queryset = Education.objects.all()

class ResumeViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    