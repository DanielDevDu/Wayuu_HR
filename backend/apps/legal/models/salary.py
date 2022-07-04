#!/usr/bin/python3

"""
--------------------------
Salary Data Model
--------------------------
"""


from django.utils.translation import gettext_lazy as _
from apps.sys_admin.models.employee import Employee
from apps.common.base_model import BaseModel
from django.db import models

class Salary(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """

    amount = models.FloatField()
    contract = models.FileField(
        upload_to="legal",
        max_length=254,
        blank=True
    )
    employee = models.ForeignKey(Employee, related_name="salary", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} employee have this {} salary".format(self.employee.id, self.amount)
