from django.test import SimpleTestCase
from django.urls import reverse, resolve
from webapp.views import home, contact, contact_list, contact_details, contact_delete, resume, my_response


class TestUrls(SimpleTestCase):

    def test_home_page(self):
        url = reverse("webapp:home")
        self.assertEqual(resolve(url).func, home)

    def test_contact_page(self):
        url = reverse("webapp:contact")
        self.assertEqual(resolve(url).func, contact)

    def test_contact_list_page(self):
        url = reverse("webapp:contact_list")
        self.assertEqual(resolve(url).func, contact_list)

    def test_contact_details_page(self):
        url = reverse("webapp:contact_details", args=[1])
        self.assertEqual(resolve(url).func, contact_details)

    def test_contact_delete_page(self):
        url = reverse("webapp:contact_delete", args=[1])
        self.assertEqual(resolve(url).func, contact_delete)

    def test_resume_page(self):
        url = reverse("webapp:resume")
        self.assertEqual(resolve(url).func, resume)

    def test_my_response_page(self):
        url = reverse("webapp:my_response", args=[1])
        self.assertEqual(resolve(url).func, my_response)
