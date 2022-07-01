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
from apps.common.base_model import BaseModel
from apps.sys_admin.models.employee import Employee
from django.utils.translation import gettext_lazy as _

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
    start_date = models.DateTimeField(
        help_text="Date when employee start in team",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when employee end in team",
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return "{}-{}".format(self.employee.__str__(), self.team.__str__())

    def delete(self):
        self.end_date = timezone.now().isoformat()

        super().delete()
    
    """class Meta:
        constraints = [
            models.UniqueConstraint(fields=['employee', 'team'], name=_('Dont repeat a team by employee'))
            ]"""