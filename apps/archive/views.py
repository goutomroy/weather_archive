import logging
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import DjangoObjectPermissions
from apps.archive.models import Archive, Observation, Task
from apps.archive.paginations import StandardResultsSetPagination
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
    * Anyone can list, view the task
    * Admin : Group - managers ->  change, view on task
    * Admin : Group - employees ->  add, change, view, delete on task
    * Api view : Manager can change(only done status) and view task
    * Api view : Employees can add(only title), view, change(only title, only owner can) and delete(only owner can) task
    """

    serializer_class = TaskSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Task.objects.all()
    permission_classes = [DjangoObjectPermissions]



