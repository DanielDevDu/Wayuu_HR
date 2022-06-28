from apps.management.models import report
from apps.record.models.education import Education
from apps.record.models.resume import Resume
from apps.sys_admin.models.employee import Employee
from apps.management.models.department import Department
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.reverse import reverse
from apps.common.serializer import BaseSerializer
from apps.record.api.serializers import ResumeSerializer

resumes = Resume.objects.all()
class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class EmployeeSerializer(BaseSerializer):

    # Add field with relationship with other tables
    #lookup_field = 'employee'

    #Custom
    full_name = serializers.SerializerMethodField()

    # Management
    roles = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="role-detail",
        many=True
    )
    departments = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="department-detail",
        many=True
    )
    """department = serializers.SerializerMethodField()"""
    teams = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="team-detail",
        many=True
    )
    reports = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="report-detail",
        many=True
    )

    # Record
    #resume = serializers.SerializerMethodField()
    #resume = serializers.StringRelatedField()
    #resume = ResumeSerializer(read_only=True)
    """resume = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="resume-detail"
        #context={'request': resumes}
    )"""
    # resume = ResumeSerializer()
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

    class Meta:
        model = Employee
        fields = '__all__' # Add all fields
        # depth=2

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation["password"]
        return representation
    
    """def get_resume(self, obj):
        other = Resume.objects.filter(employee=obj.id).first()
        request = self.context.get('request')
        url = ""
        if other:
            url = reverse("resume-detail", (other.id, ), request=request)
            print(type(url))
        return url"""

    """def get_department(self, obj):
        other = Department.objects.filter(employee=obj.id).first()
        request = self.context.get('request')
        url = ""
        if other:
            url = reverse("department-detail", (other.id, ), request=request)
        return url"""
        