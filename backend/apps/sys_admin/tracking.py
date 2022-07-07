"""
----------------------------------
Tracking, history and triggers to
Sys Admin
----------------------------------
"""

import pgtrigger
from apps.sys_admin.models import *

classes = [
    Employee,
    
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
