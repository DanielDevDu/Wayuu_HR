from apps.management.models import *
from rest_framework import serializers
from apps.common.serializer import BaseSerializer


class DepartmentSerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail",
        many=True
    )
    roles_by_department = serializers.HyperlinkedRelatedField(
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
    
class EmployeeRoleSerializer(BaseSerializer):
    role = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='full_name'
    )
    class Meta:
        model = Employee_Role
        fields = '__all__'

class EmployeeDepartmentSerializer(BaseSerializer):
    department = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='full_name'
    )
    class Meta:
        model = Employee_Department
        fields = '__all__'