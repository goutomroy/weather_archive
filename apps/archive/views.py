import logging
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from apps.archive.models import Archive, Observation, Task
from apps.archive.paginations import StandardResultsSetPagination
from apps.archive.permissions import IsOwner
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
    allowed_http_methods = ('get', 'post')


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Task.objects.all()

    def get_permissions(self):
        # only authenticated owner of task can update or delete.
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        else:
            # any authenticated user can list, retrieve tasks.
            return [IsAuthenticated()]

