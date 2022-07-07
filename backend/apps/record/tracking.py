"""
----------------------------------
Tracking, history and triggers to
Record
----------------------------------
"""

import pgtrigger
from apps.record.models import *

classes = [
    Education,
    Experience,
    Resume,
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
