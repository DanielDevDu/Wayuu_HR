import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.record.models import Resume
from admin_project.settings.base import AUTH_USER_MODEL
from apps.sys_admin.models.employee import Employee
from apps.management.models import *

logger = logging.getLogger(__name__)
# Employee and AUTH_USER_MODEL are equal

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_resume(sender, instance, created, **kwargs):
    """
    -----------------------
    After save in database
    -----------------------
    """
    if created:
        Resume.objects.create(employee=instance)
        Role.objects.create(employee=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_resume(sender, instance, **kwargs):
    instance.resume.save()
    logger.info(f"{instance}'s employee created")