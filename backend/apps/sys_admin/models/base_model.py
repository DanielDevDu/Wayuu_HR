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


class CustomQuerySet(models.QuerySet):
    def delete(self):
        self.update(status=False)
class EmployeeManager(BaseUserManager):

    """
    ---------------------------------
    Custom User Manager
    create employees
    ---------------------------------
    """

    use_for_related_fields = True

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email adrress"))

    def create_user(
        self, email, password, username, first_name, last_name, identifier, **extra_fields
        ):
        """
        -------------------------------------
        Creates and saves a User/employee with the 
        given email, identifier, password, first_name
        last_name and extra_fields
        -------------------------------------
        """
        if not identifier:
            raise ValueError(_('Users must have a valid indetifier'))
        if not first_name:
            raise ValueError(_('Users must have an First Name'))
        if not last_name:
            raise ValueError(_('Users must have an Last Name'))
        if not username:
            raise ValueError(_('Users must have a username'))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Users must have a valid email adress'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            identifier=identifier,
            username=username,
            **extra_fields

        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, password, username, first_name, last_name, identifier, **extra_fields
        ):
        """
        ------------------------------
        Creates and saves a superuser
        ------------------------------
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        # extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))

        if not password:
            raise ValueError(_("Superusers must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email address is required"))

        user = self.create_user(
            email, password, username, first_name, last_name, identifier,
            **extra_fields

        )

        user.save(using=self._db)
        return user


    
    """def status(self):
        return self.model.objects.filter(status=True)

    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)"""


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
