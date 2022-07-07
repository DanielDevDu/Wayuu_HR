import logging

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from apps.record.models import Resume
from admin_project.settings.base import AUTH_USER_MODEL
from apps.sys_admin.models.employee import Employee
from apps.management.models import *
from django.utils import timezone
from django.db.models import Q

logger = logging.getLogger(__name__)
# Employee and AUTH_USER_MODEL are equal


@receiver(post_save, sender=Employee_Role)
def set_role_employee(sender, instance, created, **kwargs):
    """
    ------------------------------------------
    - Only one role must be active
    ------------------------------------------
    """

    # Obtain the number of data
    count = sender.objects.all().count()

    # Obtain the last role (avtive) by employee
    id_old = sender.objects.filter(employee=instance.employee).filter(~Q(id=instance.id)).filter(status=True).order_by("-create_at").first()
    if id_old:
        id_old = id_old.id
    # Only if is the second role
    if created and count > 1 and id_old:

        # Set the status the previus role to False
        sender.objects.filter(id=id_old).update(
            status=False
        )

        # Set the end_date to current date
        sender.objects.filter(id=id_old).update(
            end_date=timezone.now().isoformat()
        )

@receiver(post_save, sender=Employee_Department)
def set_department_employee(sender, instance, created, **kwargs):
    """
    ------------------------------------------
    - Only one department must be active
    ------------------------------------------
    """

    # Obtain the number of data
    count = sender.objects.all().count()

    # Obtain the last role (avtive) by employee
    id_old = sender.objects.filter(employee=instance.employee).filter(~Q(id=instance.id)).filter(status=True).order_by("-create_at").first()
    if id_old:
        id_old = id_old.id
    # Only if is the second role
    if created and count > 1 and id_old:

        # Set the status the previus role to False
        sender.objects.filter(id=id_old).update(
            status=False
        )

        # Set the end_date to current date
        sender.objects.filter(id=id_old).update(
            end_date=timezone.now().isoformat()
        )

@receiver(post_save, sender=Employee_Team)
def set_department_employee(sender, instance, created, **kwargs):
    """
    ------------------------------------------
    - Only one department must be active
    ------------------------------------------
    """

    # Obtain the number of data
    count = sender.objects.all().count()

    # Obtain the last role (avtive) by employee
    id_old = sender.objects.filter(employee=instance.employee).filter(~Q(id=instance.id)).filter(status=True).order_by("-create_at").first()
    if id_old:
        id_old = id_old.id
    # Only if is the second role
    if created and count > 1 and id_old:

        # Set the status the previus role to False
        sender.objects.filter(id=id_old).update(
            status=False
        )

        # Set the end_date to current date
        sender.objects.filter(id=id_old).update(
            end_date=timezone.now().isoformat()
        )