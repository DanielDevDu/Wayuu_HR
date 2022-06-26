import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.record.models import Resume
from admin_project.settings import AUTH_USER_MODEL

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Resume.objects.create(employee=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.resume.save()
    logger.info(f"{instance}'s employee created")