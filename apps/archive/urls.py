from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.archive.views import ArchiveViewSet, ObservationViewSet

app_name = 'archive'
router = DefaultRouter()
router.register(r'archive', ArchiveViewSet, basename='archive')
router.register(r'observation', ObservationViewSet, basename='observation')


urlpatterns = [
    path('', include(router.urls)),
]