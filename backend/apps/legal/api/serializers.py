from apps.legal.models import *
from rest_framework import serializers
from apps.common.serializer import BaseSerializer


class SalarySerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail",
    )
    class Meta:
        model = Salary
        fields = '__all__'

class VacationSerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail"
    )
    class Meta:
        model = Vacation
        fields = '__all__'

class SocialSecuritySerializer(BaseSerializer):
    employee = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="employee-detail"
    )
    class Meta:
        model = SocialSecurity
        fields = '__all__'