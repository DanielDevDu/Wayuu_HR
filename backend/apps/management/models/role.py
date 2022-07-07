#!/usr/bin/python3

"""
--------------------------
Role Data Model
--------------------------
"""


from django.db import models
from django.utils import timezone
from apps.sys_admin.models import Employee
from apps.management.models.department import Department
from apps.common.base_model import BaseModel
from apps.sys_admin.models.employee import Employee
from django.utils.translation import gettext_lazy as _
from django.db.models import FilteredRelation, Q

class Role(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    name = models.CharField(max_length=100)
    job_description = models.TextField()
    default_contract = models.CharField(max_length=100, default="Pdf option")
    default_salary = models.FloatField()

    employee = models.ManyToManyField(Employee, related_name="roles", through='Employee_Role')
    department = models.ManyToManyField(Department, related_name="roles_by_department", through='Department_Role')

    def __str__(self) -> str:
        return self.name
    

class Employee_Role(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Role tables
    ----------------------------------
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    start_date = models.DateTimeField(
        help_text="Date when employee start in role",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when employee end in role",
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return "{}-{}".format(self.employee.__str__(), self.role.__str__())


    def delete(self):
        self.end_date = timezone.now().isoformat()

        super().delete()
    class Meta:
        constraints = [
            #models.UniqueConstraint(fields=['employee', 'role'], condition=Q(end_date=None), name=_('Dont repeat a role'))
            #models.UniqueConstraint(fields=['status', 'employee'], condition=Q(status=True), name=_('unique_role_active'))
        ]
    

class Department_Role(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Role tables
    ----------------------------------
    """

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(
        help_text="Date when the role was created",
        default=timezone.now
    )

    def __str__(self) -> str:
        return "Role {} in department {}".format(self.role.__str__(), self.department.__str__())
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['department', 'role'], name=_('Dont repeat a role by deparment'))
            ]
    
class Employee_Deparment_Role(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee, Department and Role tables
    ----------------------------------
    """
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    # roles = Role.objects.filter(department=department).all()
    #role_by_deparment = models.CharField(choices=roles, max_length=100)
    
    start_date = models.DateTimeField(
        help_text="Date when employee start in role",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when employee end in role",
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return "{} with role {} in {}".format(
            self.employee.__str__(),
            self.role.__str__(),
            self.department.__str__()
        )


    def delete(self):
        self.end_date = timezone.now().isoformat()

        super().delete()
