#!/usr/bin/python3

"""
--------------------------
Deparment Data Model
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

class Department(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    name = models.CharField(max_length=100)

    employee = models.ManyToManyField(Employee, through='Employee_Department', related_name="departments")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        unique_together = []
    


class Employee_Department(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Department tables
    ----------------------------------
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateTimeField(
        help_text="Date when employee start in department",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when employee end in department",
        blank=True,
        null=True
    )

    def delete(self):
        self.end_date = timezone.now().isoformat()

        super().delete()

    def __str__(self) -> str:
        return "{} in {} department".format(
            self.employee.__str__(),
            self.department.__str__()
        )
    
    """class Meta:
        unique_together = ["department", "employee"]"""