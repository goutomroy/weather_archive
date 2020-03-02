import logging

from django.contrib.auth.models import Group
from rest_framework import fields, serializers
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin
from apps.archive.models import Archive, Observation, Task

logger = logging.getLogger(__name__)


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = "__all__"


class ArchiveSerializer(serializers.ModelSerializer):
    status = fields.IntegerField(read_only=True)

    class Meta:
        model = Archive
        fields = "__all__"


class TaskSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

    def get_extra_kwargs(self):
        user = self.context['request'].user
        action = self.context['view'].action
        extra_kwargs = {}
        if user.groups.filter(name='managers').exists():
            if action in ['update', 'partial_update']:
                extra_kwargs = {'title': {'read_only': True}, 'user': {'read_only': True}}

        elif user.groups.filter(name='employees').exists():
            if action in ['create', 'update', 'partial_update']:
                extra_kwargs = {'done': {'read_only': True}, 'user': {'read_only': True}}
        return extra_kwargs

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_permissions_map(self, created):
        if self.context['view'].action == 'create':
            user = self.context['request'].user
            managers = Group.objects.get(name='managers')
            return {'change_task': [user, managers], 'delete_task': [user]}
        return {}
