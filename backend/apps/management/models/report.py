#!/usr/bin/python3

"""
--------------------------
Report Data Model
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

class Report(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    name = models.CharField(max_length=100)

    employee = models.ManyToManyField(Employee, through='Employee_Report', related_name="reports")

    def __str__(self) -> str:
        return self.name


class Employee_Report(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Department tables
    ----------------------------------
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    form = models.CharField(max_length=100, default="Here the admin should be create a form")
    file = models.CharField(max_length=100, default="pdf option")
    timestamp = models.DateTimeField(
        help_text="Date when report is assigned",
        default=timezone.now
    )

    def __str__(self) -> str:
        return "{}-{}".format(self.employee.__str__(), self.report.__str__())