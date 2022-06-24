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


class CustomQuerySet(models.QuerySet):
    def delete(self):
        self.update(status=False)
class EmployeeManager(BaseUserManager):

    use_for_related_fields = True

    def create_user(self, email, username, password=None):
        """
        -------------------------------------
        Creates and saves a User with the 
        given email, identifier and password.
        -------------------------------------
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an Username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None): 
        """
        ------------------------------
        Creates and saves a superuser
        with the given email, identifier
        and password.
        ------------------------------
        """
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


    
    def status(self):
        return self.model.objects.filter(status=True)

    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)


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
