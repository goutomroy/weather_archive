from django.contrib.auth.models import User
from django.db.models import ForeignKey, OneToOneField
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    """
    This permission expects obj has User field, otherwise it fails.
    """
    message = 'You must be the creator of this object.'

    def has_object_permission(self, request, view, obj):
        for field_object in obj._meta.fields:
            if isinstance(field_object, (ForeignKey, OneToOneField)) and field_object.remote_field.model == User:
                field_value = field_object.value_from_object(obj)
                if request.user.id == field_value:
                    return True
        return False
