#!/usr/bin/python3

"""
--------------------------
Base Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from turtle import update
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from apps.sys_admin.models.manager import EmployeeManager

class BaseModel(models.Model):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """

    use_for_related_fields = True
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(default=timezone.now, editable=False)
    update_at = models.DateTimeField(default=timezone.now, editable=False)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True
    
    objects = EmployeeManager()
    
    def delete(self):
        self.status = False
        self.save()
