from django.test import TestCase, Client
from django.urls import reverse
from webapp.models import Contact, Response
import json

class TestViews(TestCase):

    def setUp(self):
        self.contact1 = Contact.objects.create(
            first_name= "Max",
            last_name= "See",
            email= "maxsee@email.com",
            reason= "Work",
        )
        self.client = Client()
        self.contact_list_url = reverse("webapp:contact_list")
        self.contact_details_url = reverse("webapp:contact_details", args=[1])
        self.contact_delete_url = reverse("webapp:contact_delete", args=[1])
        self.contact_url = reverse("webapp:contact")
        self.home_url = reverse("webapp:home")
        self.resume_url = reverse("webapp:resume")
        self.my_response_url = reverse("webapp:response", args=[1])
        


    def test_contact_list_GET(self):
        response = self.client.get(self.contact_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "webapp/contact_list.html")
 
    def test_contact_details_GET(self):
        response = self.client.get(self.contact_details_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "webapp/contact_details.html")
#Need work on delete.
    def test_contact_delete(self):
        response = self.client.delete(self.contact_delete_url)

        self.assertEquals(response.status_code, 302)

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "webapp/home.html")
  
    def test_resume_GET(self):
        response = self.client.get(self.resume_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "webapp/resume.html")
 
    def test_contact_GET(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "webapp/contact.html")

    def test_contact_POST_add_contact(self):
        response = self.client.post(self.contact_url, {
            "first_name": "Rob",
            "last_name": "Seek",
            "email": "robseek@email.com",
            "reason": "Work",
            })
        
        contact2 = Contact.objects.get(id=2)
        self.assertEquals(contact2.first_name, "Rob")

    def test_my_response_GET(self):
        response = self.client.get(self.my_response_url)

        self.assertEquals(response.status_code, 200)

    def test_my_response_POST(self):

        response1 = self.client.post(self.my_response_url,{
            "body": "sss",
        })
        self.contact1.my_response = True
        self.assertEquals(response1.status_code, 302)
        self.assertEquals(self.contact1.my_response, True)