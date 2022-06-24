#!/usr/bin/python3

"""
--------------------------
Team Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from sys_admin.models.base_model import BaseModel
from sys_admin.models.employee import Employee

class Team(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    name = models.CharField(max_length=100)

    employee = models.ManyToManyField(Employee, through='Employee_Team', related_name="teams")

    def __str__(self) -> str:
        return self.name


class Employee_Team(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Team tables
    ----------------------------------
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(
        help_text="Date when employee was assigned to the team",
        default=timezone.now
    )

    def __str__(self) -> str:
        return "{}-{}".format(self.employee.__str__(), self.report.__str__())