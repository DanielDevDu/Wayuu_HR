from django.urls import path, include
from frontend import views
from django.contrib.auth import views as auth_views
"""
------------------------
Static Routes
------------------------
"""

urlpatterns = [
    path('', views.home , name="frontend-home"),
    #path('login/', auth_views.LoginView.as_view(template_name='frontend/login.html'), name='login'),
]