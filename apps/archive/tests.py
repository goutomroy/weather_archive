import os
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from rest_framework import status
from apps.archive.models import Task


class TestSetupClass(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client(enforce_csrf_checks=False)

    def test_is_owner_permission_on_task(self):
        """
        Only the owner of the task can delete the task.
        """
        goutom = User.objects.create_user(username='goutom', password='mdpps1234')
        bernard = User.objects.create_user(username='bernard', password='mdpps1234')
        task = Task.objects.create(title='Any task title', user=goutom)
        self.client.force_login(bernard)
        uri = f"/task/{task.id}/"
        response = self.client.delete(uri)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_archive_file_upload(self):
        file_path = os.path.join(settings.BASE_DIR, 'data/weather_archive.csv')
        with open(file_path, 'rb') as fp:
            file = SimpleUploadedFile('weather_archive.csv', fp.read())
            response = self.client.post('/archive/', format='multipart', data={'file': file})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


