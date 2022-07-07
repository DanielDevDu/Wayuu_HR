from pyexpat import model
from unicodedata import name
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.db import models

from apps.sys_admin.models import Employee


"""class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Employee
        fields = ["email", "identifier", "first_name", "last_name", "username"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = ["email", "identifier", "first_name", "last_name", "username"]
        error_class = "error"""

class CustomUserCreationForm(UserCreationForm):
    #identifier = models.BigIntegerField()
    class Meta:
        model = Employee
        fields = ('identifier',)
        error_class = "error"


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["email", "identifier", "first_name", "last_name", "username"]
        error_class = "error"