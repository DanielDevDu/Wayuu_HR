#!/usr/bin/python3

"""
--------------------------
Base Data Model
--------------------------
"""


from django.utils.translation import gettext_lazy as _
from apps.sys_admin.models.manager import EmployeeManager
from django.utils import timezone
from django.db import models
import pgtrigger
import uuid



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
    status = models.BooleanField(default=True, editable=False)

    class Meta:
        abstract = True
    
    objects = EmployeeManager()


    def update(self, *args, **kwargs):
        print("Try to update...")
        self.save()

    
    def delete(self):
        """
        ---------------------------------------------
        Custom delete method for all models:
        Don't delete anything from database,
        instead change status field to False so:
        Status = False (Data will not show)
        Status = True (Data is in use and will be show)
        ---------------------------------------------
        """
        self.status = False
        self.save()
    
    def save(self, *args, **kwargs):
        """
        -----------------------------
        Custom Save method to update
        update_at field for all models
        each time that is change
        -----------------------------
        """

        self.update_at = timezone.now().isoformat()
        super().save(*args, **kwargs)
