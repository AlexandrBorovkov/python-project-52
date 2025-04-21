from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import User


class UserCRUDTests(TestCase):
    def test_create_user(self):
        response = self.client.post(reverse("user_create"), {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'testuser@example.com'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        
    def test_update_user(self):
        user = User.objects.create_user(username='testuser', password='testpassword123', email='user@example.com')
        self.client.force_login(user)
        response = self.client.post(reverse('user_update', args=[user.id]), {
            'username': 'updateduser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'updateduser@example.com'
        })
        
        user.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.username, 'updateduser')

    def test_delete_user(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.force_login(user)
        response = self.client.post(reverse('user_delete', args=[user.id]))
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())
