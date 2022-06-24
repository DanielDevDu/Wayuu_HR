from django.urls import path, include
from frontend import views
"""
------------------------
Static Routes
------------------------
"""

urlpatterns = [
    path('', views.home , name="frontend-home"),
]