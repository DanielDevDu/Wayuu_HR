from apps.management.models import *
from rest_framework import serializers
from apps.common.serializer import BaseSerializer


class DepartmentSerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail",
        many=True
    )
    roles = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="role-detail",
        many=True
    )
    class Meta:
        model = Department
        fields = '__all__'

class RoleSerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail",
        many=True
    )
    department = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="department-detail",
        many=True
    )
    class Meta:
        model = Role
        fields = '__all__'

class ReportSerializer(BaseSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class TeamSerializer(BaseSerializer):
    class Meta:
        model = Team
        fields = '__all__'