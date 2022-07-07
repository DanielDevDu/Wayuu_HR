"""
----------------------------------
Tracking, history and triggers to
Managements
----------------------------------
"""

import pgtrigger
from apps.management.models import *

classes = [
    Department,
    Role,
    Report,
    Team,
    Employee_Department,
    Employee_Role,
    Employee_Report,
    Employee_Team,
    Department_Role,
    Employee_Deparment_Role
]


"""
--------------------------------
Don't delete data, insted change
status to False
--------------------------------
"""
for cls in classes:
    pgtrigger.register(
        pgtrigger.SoftDelete(
            name='soft_delete',
            field='status',
            value=False
        )
    )(cls)
