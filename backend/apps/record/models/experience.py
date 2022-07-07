#!/usr/bin/python3

"""
--------------------------
Experience Model of data
--------------------------
"""

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from apps.sys_admin.models.employee import Employee
from apps.common.base_model import BaseModel
from django.utils import timezone
from django.db import models


class Experience(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="experience"
    )
    job_title = models.CharField(max_length=100, default=_("developer"))
    job_description = models.TextField(default=_("job description"))
    contact_name = models.CharField(max_length=200, blank=True, default=_("reference"))
    contact_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+57324204242"
    )
    start_date = models.DateTimeField(
        help_text="Date when you start the Job",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when you finish the Job",
        default=timezone.now   
    )