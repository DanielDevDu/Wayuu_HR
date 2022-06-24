#!/usr/bin/python3

"""
--------------------------
Resume Model of data
--------------------------
"""

from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from sys_admin.models.base_model import BaseModel
from sys_admin.models.employee import Employee

class Resume(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="resume")
    personal_email = models.EmailField(max_length=254)
    description = models.TextField()
    photography = models.CharField(max_length=100, default="photo", blank=True)
    residential_address = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100)
    residencial_city = models.CharField(max_length=100)