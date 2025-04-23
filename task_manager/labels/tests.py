from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label


class LabelCRUDTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword123', email='user@example.com')
        self.client.force_login(self.user)

    def test_labels_list_view(self):
        self.label1 = Label.objects.create(name='testlabel1')
        self.label2 = Label.objects.create(name='testlabel2')
        url = reverse('list_labels')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/list_labels.html')

    def test_create_label(self):
        response = self.client.post(
            reverse("label_create"),
            {'name': 'testlabel'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name='testlabel').exists())

    def test_update_label(self):
        label = Label.objects.create(name='testlabel')
        response = self.client.post(reverse('label_update', args=[label.id]), {
            'name': 'updatedlabel',
        })

        label.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(label.name, 'updatedlabel')

    def test_delete_label(self):
        label = Label.objects.create(name='testlabel')
        response = self.client.post(reverse('label_delete', args=[label.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(name='testlabel').exists())
