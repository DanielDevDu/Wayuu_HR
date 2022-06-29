from ast import Return
from multiprocessing import Condition, context
from apps.sys_admin.models.employee import Employee
from apps.management.models.role import Employee_Role
from apps.sys_admin.models import Employee
from rest_framework import viewsets, permissions
from apps.sys_admin.api.serializers import EmployeeReadSerializer, EmployeeWriteSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.record.models import *
from apps.record.api.serializers import ResumeSerializer
# Lead Viewset
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class IsOwnerOrSuperUser(permissions.BasePermission):
    """
    ---------------------------------------------------
    Conly self employees, staff and superuser can 
    update and delete the data of the employee
    Only authenticated can view data
    The staff can't update data
    ---------------------------------------------------
    """
    edit_methods = ("PUT", "PATCH")
    # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.user.is_superuser:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        if obj == request.user and request.method in permissions.SAFE_METHODS:
            return True

        """if request.method in permissions.SAFE_METHODS:
            return False"""

        return False


class EmployeeViewSet(viewsets.ModelViewSet):
#class EmployeeViewSet(generics.ListAPIView):
    permission_classes = [
         IsOwnerOrSuperUser
    ]
    action_serializer_classes = {
      "create": EmployeeReadSerializer,
      "update": EmployeeWriteSerializer,
      "retrieve": EmployeeReadSerializer,
      "list": EmployeeReadSerializer,
      "partial_update": EmployeeWriteSerializer,
     }
    def get_serializer_class(self):
        return self.action_serializer_classes[self.action]

    employees = Employee.objects.all()
    queryset = employees

    """@action(detail=True, methods=["GET"], url_path='roles')
    def roles(self, request, pk=None):
        employee = self.get_object()
        roles = employee.roles.all()
        return Response([role.name for role in roles])"""

    @action(detail=False, methods=["GET"], url_path='active')
    def empleyee_active(self, request):
        data = self.queryset.filter(status=True)
        serializer_context = {'request': request}
        serializer = EmployeeWriteSerializer(data, many=True, context=serializer_context)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        current_user_id = str(request.user.id)

        queryset = Employee.objects.filter(id=pk)
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data[0])
        #return super().retrieve(request, current_user_id)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    """def pre_save(self, obj):
        obj.employee = self.request.user"""

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer
    queryset = []
    print("Yeaaaaahh")
    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""
        print(ObtainAuthToken())
        return Response(request.data)