from django.test import TestCase, Client
from django.urls import reverse
from webapp.models import Contact, Response

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.contact_list_url = reverse("webapp:contact_list")
        self.contact_url = reverse("webapp:contact")
        


    def test_contact_list_GET(self):
        response = self.client.get(self.contact_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "webapp/contact_list.html")
  
    def test_contact_GET(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "webapp/contact.html")

    def test_contact_POST_add_contact(self):
        url = reverse("webapp:contact")
        response = self.client.post(url, {
            "first_name": "Rob",
            "last_name": "Seek",
            "email": "robseek@email.com",
            "reason": "Work",
            "my_response": True,
            "body": "some text"
            })
        
        contact1 = Contact.objects.get(id=1)
        self.assertEquals(contact1.first_name, "Rob")