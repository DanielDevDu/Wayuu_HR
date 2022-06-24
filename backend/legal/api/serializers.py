from legal.models import *
from rest_framework import serializers


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'

class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = '__all__'

class SocialSecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialSecurity
        fields = '__all__'