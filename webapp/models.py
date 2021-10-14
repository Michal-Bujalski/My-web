from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    reason = models.CharField(max_length=254)
    my_response = models.BooleanField(
        default=False, verbose_name="Did I response")
    body = models.TextField(blank=True, null=True)
    created = models.TimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Response(models.Model):

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.TimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return f"{self.contact}"
