from apps.sys_admin.models.employee import Employee
from apps.management.models.role import Employee_Role
from apps.sys_admin.models import Employee
from rest_framework import viewsets
from apps.sys_admin.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.record.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from apps.sys_admin.exceptions import ErrorLogin, ErrorPassword
from apps.sys_admin.permissions import IsOwnerOrSuperUser


class EmployeeViewSet(viewsets.ModelViewSet):
#class EmployeeViewSet(generics.ListAPIView):
    #lookup_field = "indetifier"
    permission_classes = [
         IsOwnerOrSuperUser,
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

    @action(detail=False, methods=["GET"], url_path='active')
    def empleyee_active(self, request):
        data = self.queryset.filter(status=True)
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer(data, many=True, context=serializer_context)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path='inactive')
    def empleyee_inactive(self, request):
        data = self.queryset.filter(status=False)
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer(data, many=True, context=serializer_context)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path='<int:identifier>')
    def retrieve_by_idetifier(self, request, identifier):
        current_user_id = str(request.user.id)

        queryset = Employee.objects.filter(identifier=identifier)
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data[0])

    def retrieve(self, request, pk=None):
        current_user_id = str(request.user.id)

        queryset = Employee.objects.filter(id=pk)
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data[0])
        #return super().retrieve(request, current_user_id)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @action(detail=False, methods=["POST"], url_path='update_password')
    def empleyee_update_password(self, request):
        data = self.queryset.filter(status=True)
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer(data, many=True, context=serializer_context)
        return Response(serializer.data)
    

class LoginViewSet(viewsets.ViewSet):
    """
    ----------------
    Login employee.
    ----------------
    """

    serializer_class = EmployeeLoginSerializer
    queryset = []

    def create(self, request):
        """
        -------------------------------
        Use the ObtainAuthToken APIView 
        to validate and create a token.
        -------------------------------
        """

        # Get request data
        email = request.POST.get("email")
        password = request.POST.get("password")

        # obtain employee object
        try:
            employee = Employee.objects.get(email=email)
        except Employee.DoesNotExist:
            raise ErrorLogin

        # check password
        pwd_valid = check_password(password, employee.password)
        if not pwd_valid or pwd_valid is None:
            raise ErrorPassword

        # Check authenticate employee
        employee = authenticate(request, username=email, password=password)
        if employee is not None:
            # Login employee
            login(request, employee)
            return Response({'detail': "Login success"}, 200)
        return ErrorLogin

        # optional ? return employee's data serialized
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer([employee], many=True, context=serializer_context)

        

class LogoutViewSet(viewsets.ViewSet):
    """
    ----------------
    Logout employee.
    ----------------
    """

    serializer_class = None
    queryset = []

    def create(self, request):
        """
        -------------------------------
        Use Logout method to logout
        -------------------------------
        """

        logout(request)

        return Response({'detail': "Logout success"}, 200)
        