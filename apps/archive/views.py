import logging
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from apps.archive.models import Archive, Observation, Task
from apps.archive.paginations import StandardResultsSetPagination
from apps.archive.permissions import IsTaskOwner
from apps.archive.serializers import ArchiveSerializer, ObservationSerializer, TaskSerializer

logger = logging.getLogger(__name__)


class ObservationViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ObservationSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Observation.objects.all()


class ArchiveViewSet(viewsets.ModelViewSet):

    serializer_class = ArchiveSerializer
    parser_classes = (MultiPartParser,)
    pagination_class = StandardResultsSetPagination
    queryset = Archive.objects.all()
    http_method_names = ('get', 'post')


class TaskViewSet(viewsets.ModelViewSet):

    """
    Only authenticated owner of task can update or delete.
    Any authenticated user can list, retrieve tasks.
    """

    serializer_class = TaskSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Task.objects.all()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsTaskOwner()]
        else:
            return [IsAuthenticated()]


