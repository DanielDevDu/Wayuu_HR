#!/usr/bin/python3

"""
--------------------------
Education Model of data
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

class Education(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="education")
    education_title = models.CharField(max_length=100)
    university = models.CharField(max_length=200)
    start_date = models.DateTimeField(help_text="Date when you start the Job")
    end_date = models.DateTimeField(help_text="Date when you finish the Job")