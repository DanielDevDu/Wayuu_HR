from rest_framework import viewsets, permissions

"""
--------------------------------
Permission for the employees
--------------------------------
"""


class IsOwnerOrSuperUser(permissions.BasePermission):
    """
    ---------------------------------------------------
    Conly self employees, staff and superuser can 
    update and delete the data of the employee
    Only authenticated can view data
    The staff can't update data
    ---------------------------------------------------
    """
    edit_methods = ("PUT", "PATCH")
    # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.user.is_superuser:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True
        print(obj.id, request.user.id)
        if obj.id == request.user.id and request.method in permissions.SAFE_METHODS:
            return True

        """if request.method in permissions.SAFE_METHODS:
            return False"""

        return False
