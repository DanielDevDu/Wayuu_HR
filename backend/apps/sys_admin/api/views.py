from multiprocessing import context
from apps.sys_admin.models.employee import Employee
from apps.management.models.role import Employee_Role
from rest_framework import viewsets, permissions
from apps.sys_admin.api.serializers import EmployeeSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Lead Viewset


class EmployeeViewSet(viewsets.ModelViewSet):
#class EmployeeViewSet(generics.ListAPIView):
    """permission_classes = [
         permissions.IsAuthenticated,
    ]"""
    serializer_class = EmployeeSerializer

    #employees = Employee.objects.all().filter(status=True)
    employees = Employee.objects.all()
    queryset = employees

    @action(detail=True, methods=["GET"], url_path='roles')
    def roles(self, request, pk=None):
        employee = self.get_object()
        roles = employee.roles.all()
        return Response([role.name for role in roles])
    
    def list(self, request):
        queryset = Employee.objects.all()
        serializer_context = {'request': request}
        serializer = EmployeeSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        print("Destroy?----")
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    

    