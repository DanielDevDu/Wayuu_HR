from django.urls import path, include
from frontend import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from apps.sys_admin.api.views import *
"""
------------------------
Static Routes
------------------------
"""

urlpatterns = [
    path('', views.home , name="frontend-home"),
    #path('login/', LoginViewSet.as_view({'get': 'create'}), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='frontend/login.html'), name='login'),
]