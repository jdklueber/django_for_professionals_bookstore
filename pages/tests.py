from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

class HomePageTests(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_home_page_view_by_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_template_used(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, "Homepage")
    
    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_home_page_resolves_correctly(self):
        view = resolve('/')
        self.assertEquals(view.func.__name__, HomePageView.as_view().__name__)