#!/usr/bin/python3

"""
--------------------------
Education Model of data
--------------------------
"""

from django.utils.translation import gettext_lazy as _
from apps.sys_admin.models.employee import Employee
from apps.common.base_model import BaseModel
from django.utils import timezone
from django.db import models

class Education(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="education"
    )
    education_title = models.CharField(max_length=100, default=_("developer"))
    university = models.CharField(max_length=200, default=_("University"))
    start_date = models.DateTimeField(
        help_text="Date when you start the Job",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when you finish the Job",
        default=timezone.now   
    )