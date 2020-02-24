from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.archive.views import ArchiveViewSet

app_name = 'archive'
router = DefaultRouter()
router.register(r'', ArchiveViewSet, basename='archive')


urlpatterns = [
    path('', include(router.urls)),
]