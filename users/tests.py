from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='me', email='you@you.com', password='Passw0rd!')
        self.assertEqual(user.username, 'me')
        self.assertEqual(user.email, 'you@you.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(username='testsuperadmin', email='holy@cow.com', password='Passw0rd!')
        self.assertEqual(user.username, 'testsuperadmin')
        self.assertEqual(user.email, 'holy@cow.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
