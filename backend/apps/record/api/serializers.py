"""
--------------------------------
Serializers class Employee Model
--------------------------------
"""


from apps.common.serializer import BaseSerializer
from apps.sys_admin.models import Employee
from rest_framework import serializers
from apps.record.models import *


class EducationSerializer(BaseSerializer):
    """ 
    --------------------------------------------
    Serialize Education Model with all fields
    Methods: all
    Enpoints: 
        - api/education
        - api/education/id_education
    --------------------------------------------
    """

    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='full_name'
    )
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(BaseSerializer):
    """ 
    --------------------------------------------
    Serialize Experience Model with all fields
    Methods: all
    Enpoints: 
        - api/experience
        - api/experience/id_experience
    --------------------------------------------
    """

    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='full_name'
    )
    class Meta:
        model = Experience
        fields = '__all__'

class ResumeSerializer(BaseSerializer):
    """ 
    --------------------------------------------
    Serialize Resume Model with all fields
    Methods: GET, POST
    Enpoints: 
        - api/resume
        - api/resume/id_resume
    --------------------------------------------
    """

    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='relation'
    )
    class Meta:
        model = Resume
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if not instance.employee.is_staff:
    #         representation.clear()
    #     return representation
    
class ResumeUpdateSerializer(BaseSerializer):
    """ 
    --------------------------------------------
    Serialize Resume Model with all fields
    Methods: PUT
    Enpoints: 
        - api/resume
        - api/resume/id_resume
    --------------------------------------------
    """
    
    employee = serializers.SlugRelatedField( 
        read_only=True,
        slug_field='relation'
    )
    class Meta:
        model = Resume
        fields = "__all__"
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if not instance.employee.is_staff:
    #         representation.clear()
    #     return representation