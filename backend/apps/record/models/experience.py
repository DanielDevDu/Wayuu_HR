#!/usr/bin/python3

"""
--------------------------
Experience Model of data
--------------------------
"""

from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from apps.sys_admin.models.base_model import BaseModel
from apps.sys_admin.models.employee import Employee

class Experience(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="experience")
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    contact_name = models.CharField(max_length=200, blank=True)
    contact_number = models.CharField(max_length=200, blank=True)
    start_date = models.DateTimeField(help_text="Date when you start the Job")
    end_date = models.DateTimeField(help_text="Date when you finish the Job")