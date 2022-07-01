#!/usr/bin/python3

"""
--------------------------
Social Security Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from turtle import back
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from apps.common.base_model import BaseModel
from apps.sys_admin.models.employee import Employee
from django.utils.translation import gettext_lazy as _

class SocialSecurity(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    # Ono to many relationship
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="socialsecurity")
    pension = models.CharField(max_length=100, default="pensio", blank=True)
    insurance = models.CharField(max_length=100,default="Arl", blank=True)
    mandatory_healthcare_provider = models.CharField(max_length=100, default="eps", blank=True)
    private_healthcare_provider = models.CharField(max_length=100, default="private eps", blank=True)
    note = models.TextField(default = "The employee has no illnesses to report")
    file = models.FileField(upload_to="legal",verbose_name=_("Social Security pdf"), blank=True)

    def __str__(self) -> str:
        return "{} {}'s Social Security".format(self.employee.first_name, self.employee.last_name)