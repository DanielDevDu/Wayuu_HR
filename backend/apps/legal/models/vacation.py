#!/usr/bin/python3

"""
--------------------------
Vacation Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from apps.common.base_model import BaseModel
from apps.sys_admin.models.employee import Employee

class Vacation(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="vacation")
    start_date = models.DateTimeField(help_text="Start of vacations")
    end_date = models.DateTimeField(help_text="End of vacations")