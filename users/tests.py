from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .views import SignupPageView

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
    
class SignupPageTests(TestCase):
    username = 'testola'
    email = 'testola@testola.org'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user( self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        test_user = get_user_model().objects.all()[0]
        self.assertEqual(test_user.username, self.username)
        self.assertEqual(test_user.email, self.email)