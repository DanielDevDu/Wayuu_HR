from apps.record.models import *
from apps.sys_admin.models import Employee
from rest_framework import serializers
from rest_framework.reverse import reverse
from django.urls import resolve
from apps.common.serializer import BaseSerializer

class EducationSerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail"
    )
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail"
    )
    class Meta:
        model = Experience
        fields = '__all__'

class ResumeSerializer(BaseSerializer):
    #employee = serializers.SerializerMethodField()
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail"
    )
    class Meta:
        model = Resume
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not instance.employee.is_staff:
            representation.clear()
        return representation

    """def get_employee(self, obj):
        request = self.context.get('request')
        base_url =  "{0}://{1}{2}{3}".format(request.scheme, request.get_host(), request.path, obj.pk)
        print(base_url)
        return request.build_absolute_uri() + str(obj.id)"""
    
class ResumeUpdateSerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail"
    )
    class Meta:
        model = Resume
        fields = ["City"]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not instance.employee.is_staff:
            representation.clear()
        return representation