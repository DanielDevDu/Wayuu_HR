
from apps.management.models import *
from rest_framework import serializers
from apps.common.serializer import BaseSerializer
from rest_framework.response import Response
from django.db.models import FilteredRelation, Q


class DepartmentSerializer(BaseSerializer):
    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='relation',
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
    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='full_name',
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
    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='full_name',
        many=True
    )
    class Meta:
        model = Report
        fields = '__all__'

class TeamSerializer(BaseSerializer):
    employee = serializers.SlugRelatedField(
        read_only=True,
        slug_field='full_name',
        many=True
    )
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
        slug_field='relation'
    )

    co_workers = serializers.SerializerMethodField()
    class Meta:
        model = Employee_Department
        fields = "__all__"

    
    def get_co_workers(self, obj):
        """
        ----------------------------------
        Query to obtain active coworkers
        in current department
        ----------------------------------
        """

        employees = Employee_Department.objects\
                        .filter(status=True)\
                        .filter(department=obj.department)\
                        .filter(~Q(employee=obj.employee))\
                        .all()

        response = [{
            "full_name": "{}".format(employee.employee.full_name),
            "email": "{}".format(employee.employee.email),
            "identifier": "{}".format(employee.employee.identifier)
        } for employee in employees]

        return response