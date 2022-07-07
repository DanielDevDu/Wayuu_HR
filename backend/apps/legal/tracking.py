"""
----------------------------------
Tracking, history and triggers to
Legal
----------------------------------
"""

import pgtrigger
from apps.legal.models import *

classes = [
    Salary,
    SocialSecurity,
    Vacation
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
