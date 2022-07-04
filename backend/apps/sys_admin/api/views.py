"""
-----------------------------------
Employeee, Login, Logout and change
password Views (Enpoints) of API
-----------------------------------
"""
from apps.sys_admin.models.employee import Employee
from apps.sys_admin.models import Employee
from rest_framework import viewsets, permissions, status, generics
from apps.sys_admin.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.record.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from apps.sys_admin.exceptions import ErrorLogin, ErrorPassword
from apps.sys_admin.permissions import IsOwnerOrSuperUser


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    -----------------------------------
    Employeee Views (Enpoints) of API
    enpoints:
        - api/employee
        - api/employee/indentifier
    methods:
        - all
    -----------------------------------
    """
    #lookup_field = "indetifier"

    lookup_field = "identifier"

    permission_classes = [
         IsOwnerOrSuperUser,
    ]
    action_serializer_classes = {
      "create": EmployeeCreateSerializer,
      "update": EmployeeUpdateSerializer,
      "retrieve": EmployeeReadSerializer,
      "list": EmployeeReadSerializer,
      "partial_update": EmployeeUpdateSerializer,
      "employee_change_password": ChangePasswordSerializer,
     }
    def get_serializer_class(self):
        # What serializer use?
        return self.action_serializer_classes[self.action]

    employees = Employee.objects.all()
    queryset = employees

    @action(detail=False, methods=["GET"], url_path='active',lookup_field = "identifier")
    def empleyee_active(self, request):
        """
        -----------------------------------------
        Enpoitn that return only active employees
        in: /api/employee/active
        list
        Methods: GET
        -----------------------------------------
        """
        data = self.queryset.filter(status=True)
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer(data, many=True, context=serializer_context)
        return Response(serializer.data)
    
    # @action(detail=True, methods=["GET"], url_path='resume',lookup_field = "identifier")
    # def empleyee_resume(self, request, identifier=None):
    #     data = self.queryset.get(identifier=identifier)
    #     serializer_context = {'request': request}
    #     serializer = ResumeSerializer(data, context=serializer_context)
    #     return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path='inactive')
    def empleyee_inactive(self, request):
        """
        -------------------------------------------
        Enpoitn that return only inactive employees
        in: /api/employee/inactive
        list
        Methods: GET
        -------------------------------------------
        """
        data = self.queryset.filter(status=False)
        serializer_context = {'request': request}
        serializer = EmployeeReadSerializer(data, many=True, context=serializer_context)
        return Response(serializer.data)

    
    @action(detail=True, methods=["post"],  url_path='change_password', permission_classes=[IsOwnerOrSuperUser])
    def employee_change_password(self, request, identifier=None):
        """
        -------------------------------------------
        Enpoitn that let us change employee password
        in: /api/employee/identifier/change_password
        retrive
        Methods: POST
        -------------------------------------------
        """

        # Obtain the object
        employee = self.get_object()
        serializer_context = {'user': request.user}
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check the user (only the issefl can change the password)
            if employee is not request.user:
                raise serializers.ValidationError({
                    "permissions": "You do not have permissions to change the password"
                }) 
            
            # Check old password
            old_password = request.data["old_password"]
            if not employee.check_password(old_password):
                raise serializers.ValidationError({
                    "old_password": "Old password is not correct"
                })  
            
            # set the new password
            employee.set_password(serializer.validated_data['password'])
            employee.save()

            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    

class LoginViewSet(viewsets.ViewSet):
    """
    --------------------------------
    Login employee.
    enpoints: api/login
    retrive
    Methods: POST
    --------------------------------
    """

    serializer_class = EmployeeLoginSerializer
    queryset = []

    def create(self, request):
        """
        -------------------------------
        Use the ObtainAuthToken APIView 
        to validate and create a token.
        Methods: POST
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
            return Response({
                "id": employee.id,
                "email":email,
                "identifier":employee.identifier,
                "full_name": employee.full_name
            })
        return ErrorLogin

class LogoutViewSet(viewsets.ViewSet):
    """
    --------------------------------
    Logout employee.
    enpoints: api/logout
    retrive
    Methods: POST
    --------------------------------
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
