"""
-----------------------------------
Experience, Education, Resume 
Views (Enpoints) of API
-----------------------------------
"""
from apps.record.models import *
from rest_framework import viewsets, permissions
from apps.record.api.serializers import *

# Lead Viewset


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    -----------------------------------
    Experience Views (Enpoints) of API
    enpoints:
        - api/experience
        - api/employee/id_experience
    methods:
        - all
    -----------------------------------
    """
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

class EducationViewSet(viewsets.ModelViewSet):
    """
    -----------------------------------
    Education Views (Enpoints) of API
    enpoints:
        - api/education
        - api/education/id_education
    methods:
        - all
    -----------------------------------
    """
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = EducationSerializer
    queryset = Education.objects.all()

class ResumeViewSet(viewsets.ModelViewSet): 
    """
    -----------------------------------
    Resume Views (Enpoints) of API
    enpoints:
        - api/resume
        - api/resume/id_resume
    methods:
        - get, put, head, options
    -----------------------------------
    """
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    action_serializer_classes = {
      "create": ResumeSerializer,
      "update": ResumeUpdateSerializer,
      "retrieve": ResumeSerializer,
      "list": ResumeSerializer,
      "partial_update": ResumeUpdateSerializer,
     }
    def get_serializer_class(self):
        # What serializer use?
        return self.action_serializer_classes[self.action]

    queryset = Resume.objects.all()
    http_method_names = ['get', 'put', 'head', 'options']
    