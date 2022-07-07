#!/usr/bin/python3
"""
--------------------------
Resume Model of data
--------------------------
"""


from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from apps.sys_admin.models.employee import Employee
from django_countries.fields import CountryField
from apps.common.base_model import BaseModel
from django.db import models


class Resume(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """

    class Gender(models.TextChoices):
        MALE = "Male", _("Male")
        FEMALE = "Female", _("Female")
        OTHER = "Other", _("Other")
    
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="resume"
    )
    personal_email = models.EmailField(max_length=254, default="personal email")
    description = models.TextField(
        verbose_name=_("Description"), default=_("A brief description about yourself")
    )
    residential_address = models.CharField(max_length=200, default="address")
    country = CountryField(verbose_name=_("Country"), default="COL")
    city = models.CharField(verbose_name=_("City"), max_length=100, default="Medellin")
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+57324204242"
    )
    photography = models.ImageField(
        upload_to="resume",
        verbose_name=_("Profile Photo"), default="fotoperfil.jpeg"
    )
    gender = models.CharField(
        verbose_name=_("Gender"), max_length=20, choices=Gender.choices, default=Gender.OTHER
    )

    def __str__(self) -> str:
        return "{}'s resume".format(self.employee.full_name)