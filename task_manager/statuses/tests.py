from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status


class StatusCRUDTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword123', email='user@example.com')
        self.client.force_login(self.user)

    def test_statuses_list_view(self):
        self.status1 = Status.objects.create(name='teststatus1')
        self.status2 = Status.objects.create(name='teststatus2')
        url = reverse('list_statuses')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/list_statuses.html')

    def test_create_status(self):
        response = self.client.post(
            reverse("status_create"),
            {'name': 'teststatus'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='teststatus').exists())

    def test_update_status(self):
        status = Status.objects.create(name='teststatus')
        response = self.client.post(reverse('status_update', args=[status.id]), {
            'name': 'updatedstatus',
        })
        
        status.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(status.name, 'updatedstatus')

    def test_delete_status(self):
        status = Status.objects.create(name='teststatus')
        response = self.client.post(reverse('status_delete', args=[status.id]))
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(name='teststatus').exists())
