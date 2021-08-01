from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    reason = models.CharField(max_length=254)
    # contact = models.BooleanField(default=False, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"