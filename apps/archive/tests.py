from django.contrib.auth.models import User
from django.test import TestCase, Client
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
        self.assertEqual(response.status_code, 403)
