#!/usr/bin/python3

"""
--------------------------
Vacation Data Model
--------------------------
"""


from apps.sys_admin.models.employee import Employee
from apps.common.base_model import BaseModel
from django.utils import timezone
from django.db import models

class Vacation(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="vacation")
    start_date = models.DateTimeField(
        help_text="Date when you start the vacations",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when you finish the vacations",
        default=timezone.now   
    )

    # Make method that return work days 