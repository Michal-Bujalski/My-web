from django.test import TestCase, SimpleTestCase
from webapp.models import Contact

# Create your tests here.

class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(
            first_name= "Rob",
            last_name= "Seek",
            email= "robseek@email.com",
            reason= "Work",
            my_response= True,
            body= "some text",
        )

    def test_contacts_email(self):
        rob = Contact.objects.get(first_name= "Rob")
        self.assertEqual(rob.first_name, "Rob")
        self.assertEqual(rob.last_name, "Seek")
        self.assertEqual(rob.email, "robseek@email.com")
