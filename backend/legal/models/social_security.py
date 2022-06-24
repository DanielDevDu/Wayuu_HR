#!/usr/bin/python3

"""
--------------------------
Social Security Data Model
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

class SocialSecurity(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="social_security")
    pension = models.CharField(max_length=100, default="pdf option?")
    insurance = models.CharField(max_length=100,default="pdf option?")
    mandatory_healthcare_provider = models.CharField(max_length=100, default="eps?")
    private_healthcare_provider = models.CharField(max_length=100, default="eps?", blank=True)
    note = models.TextField(default = "The employee has no illnesses to report")