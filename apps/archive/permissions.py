import logging
from rest_framework.permissions import BasePermission

logger = logging.getLogger(__name__)


class IsTaskOwner(BasePermission):

    """
    This permission expects obj has User field, named 'user', otherwise it fails.
    """
    message = 'You must be the creator of this object.'

    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('change_delete_task', obj)

