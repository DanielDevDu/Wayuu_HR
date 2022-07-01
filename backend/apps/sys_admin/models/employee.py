#!/usr/bin/python3

"""
--------------------------
Employee-user Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
import uuid
import pghistory
import pgtrigger
from apps.sys_admin.models.manager import EmployeeManager
from django.utils.translation import gettext_lazy as _
from apps.common.base_model import BaseModel

class Employee(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    ----------------------------------
    Create Table in Postgres Database
    User Model for the App
    ----------------------------------
    """

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    last_name_second = models.CharField(max_length=100, blank=True)
    identifier = models.BigIntegerField()
    email = models.EmailField(max_length=254, unique=True, blank=True)
    username = models.CharField(max_length=100, unique=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #is_admin = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)

    #data_joined = models.DateTimeField(default=timezone.now)
    #last_login = models.DateTimeField(verbose_name="date joined", auto_now=True, editable=False)

    # Many to Many Relationships
    #from management.models.department import Department
    

    
    USERNAME_FIELD = "email" # Field to login
    REQUIRED_FIELDS = ["first_name", "last_name", "identifier", "username"] # Field needs to create
    
    objects = EmployeeManager()

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
        ordering = ["is_active", "first_name", "last_name"]

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)
    
    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    
    def save(self, *args, **kwargs):
        """
        ------------------------------------------
        Custom svae method to create a custom and
        unique email and username for each employee
        ------------------------------------------
        """
        count = Employee.objects.all().count()
        self.email = "{}.{}{}{}@gmail.com".format(
            self.first_name,
            self.last_name,
            str(count),
            str(self.identifier)[-1])
        
        self.username = self.email.split("@")[0]
        super().save(*args, **kwargs)
    
    """def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True"""
