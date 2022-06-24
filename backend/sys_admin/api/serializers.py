from management.models import report
from record.models.education import Education
from sys_admin.models.employee import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):

    # Add field with relationship with other tables

    # Management
    roles = serializers.StringRelatedField(many=True)
    departments = serializers.StringRelatedField(many=True)
    teams = serializers.StringRelatedField(many=True)
    reports = serializers.StringRelatedField(many=True)

    # Record
    """resume = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="resume-detail"
    )"""
    education = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="education-detail"
    )
    experience = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="experience-detail"
    )

    # Legal
    salary = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="salary-detail"
    )
    social_security = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="social_security-detail"
    )
    vacation = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="vacation-detail"
    )

    class Meta:
        model = Employee
        fields = '__all__' # Add all fields