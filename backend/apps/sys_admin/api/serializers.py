"""
--------------------------------
Serializers class Employee Model
--------------------------------
"""

from apps.record.models.resume import Resume
from apps.sys_admin.models.employee import Employee
from apps.management.models.department import Employee_Department
from apps.management.models.role import Employee_Role
from rest_framework import serializers
from apps.common.serializer import BaseSerializer
from apps.management.api.serializers import *
from django.contrib.auth.password_validation import validate_password


class EmployeeReadSerializer(BaseSerializer):
    """ 
    --------------------------------------------
    Serialize Employee Model with all fields
    This work for Read Methods of request
    List and Detail 
    --------------------------------------------
    """

    lookup_field = 'identifier'

    # Custom Fields 
    full_name = serializers.SerializerMethodField()

    ### Serialize relationships ###

    # Management
    # roles = RoleSerializer(many=True, read_only=True)
    # departments = DepartmentSerializer(many=True, read_only=True)
    # teams = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="team-detail",
    #     many=True
    # )
    # reports = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="report-detail",
    #     many=True
    # )

    # Record
    resume = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="resume-detail"
        #context={'request': resumes}
    )
    education = serializers.HyperlinkedIdentityField(
        view_name="education-detail",
        read_only=True,
        many=True
    )
    experience = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="experience-detail",
        many=True
    )

    # Legal
    salary = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="salary-detail"
    )
    socialsecurity = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="socialsecurity-detail",
        many=True
    )
    vacation = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="vacation-detail",
        many=True
    )

    # Intermediate tables
    employee_role = serializers.SerializerMethodField()
    employee_department = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__' # Add all fields

    def get_full_name(self, obj):
        """
        -----------------------------------------
        Custom methos to add fiel in the response
        -----------------------------------------
        """
        return f'{obj.first_name} {obj.last_name}'

    def to_representation(self, instance):
        """
        --------------------------------------
        Method manage the json representation
        fields in the api
        -------------------------------------
        """
        representation = super().to_representation(instance)
        del representation["password"] # Don't show the password
        return representation
    
    def get_employee_role(self, obj):
        role_by_employee = Employee_Role.objects.filter(employee=obj.id).all()
        serializer = EmployeeRoleSerializer(role_by_employee, many=True)
        return serializer.data

    def get_employee_department(self, obj):
        department_by_employee = Employee_Department.objects.filter(employee=obj.id).all()
        serializer = EmployeeDepartmentSerializer(department_by_employee, many=True)
        return serializer.data 
    

class EmployeeCreateSerializer(BaseSerializer):
    """
    ---------------------------------------
    Class to serializer only update method
    ---------------------------------------
    """
    class Meta:
        model = Employee
        # What fields are allowed to update? and for who?
        fields = [
            "first_name",
            "last_name",
            "identifier",
            "email",
            "password"]
        read_only_fields = ["email"]
        
    
    # def create(self, validated_data):
    #     """
    #     -------------------------------
    #     Custom post method to create
    #     employees
    #     -------------------------------
    #     """
    #     # Create employee
    #     employee = Employee(**validated_data)
    #     employee.set_password(validated_data['password'])
    #     employee.save()
    #     return employee

    def to_representation(self, instance):
        """
        --------------------------------------
        Method manage the json representation
        fields in the api
        -------------------------------------
        """
        representation = super().to_representation(instance)
        del representation["password"] # Don't show the password
        return representation
class EmployeeUpdateSerializer(BaseSerializer):
    """
    ---------------------------------------
    Class to serializer only update method
    ---------------------------------------
    """
    class Meta:
        model = Employee
        # What fields are allowed to update? and for who?
        exclude = [
            "first_name",
            "last_name",
            "identifier",
            "password",
            "email",
            "username",
            "is_superuser",
            "is_active",
            "last_login"
        ]
        
class EmployeeLoginSerializer(BaseSerializer):
    """
    ---------------------------------------
    Class to serializer only update method
    ---------------------------------------
    """
    class Meta:
        model = Employee
        # What fields are allowed to update? and for who?
        fields = [
            "email",
            "password"]
    
    def to_representation(self, instance):
        """
        --------------------------------------
        Method manage the json representation
        fields in the api
        -------------------------------------
        """
        representation = super().to_representation(instance)
        del representation["password"] # Don't show the password
        return representation

class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    -----------------------------------------
    Class to serializer only change password
    -----------------------------------------
    """
    # lookup_field = 'identifier'

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Employee
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
