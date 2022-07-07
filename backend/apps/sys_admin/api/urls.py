from rest_framework import routers
from apps.sys_admin.api.views import EmployeeViewSet
from django.urls import path, include

urlpatterns = [
    #path("", include(router.urls), name="employees")
    path("employees", EmployeeViewSet.as_view(), name="employees")
]