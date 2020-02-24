import logging
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from apps.archive.models import Archive
from apps.archive.paginations import StandardResultsSetPagination
from apps.archive.serializers import ArchiveSerializer

logger = logging.getLogger(__name__)


class ArchiveViewSet(viewsets.ModelViewSet):

    serializer_class = ArchiveSerializer
    parser_classes = [FileUploadParser]
    pagination_class = StandardResultsSetPagination
    queryset = Archive.objects.all()
    allowed_http_methods = ('get', 'post')

    # def get_queryset(self):
    #     return Archive.objects.all()

    # @action(detail=False, methods=['post'])
    # def upload(self, request):
    #     file_serializer = ArchiveSerializer(data=request.data, context={"request": request})
    #     if file_serializer.is_valid():
    #         file_serializer.save()
    #         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

