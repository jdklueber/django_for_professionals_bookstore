from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

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
    
    def test_home_page_resolves_correctly(self):
        view = resolve('/')
        self.assertEquals(view.func.__name__, HomePageView.as_view().__name__)

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get(reverse('about'))

    def test_home_page_view_by_url(self):
        response = self.client.get('/about')
        self.assertEquals(response.status_code, 200)

    def test_home_page_template_used(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, "About")
    
    def test_home_page_resolves_correctly(self):
        view = resolve('/about')
        self.assertEquals(view.func.__name__, AboutPageView.as_view().__name__)