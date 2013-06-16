from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    date_of_birth = models.DateField(default='1970-01-01')
    bio = models.TextField(max_length=1000, blank=True)
    jid = models.CharField(max_length=254, blank=True)
    skype_id = models.CharField(max_length=254, blank=True)
    other_contacts = models.TextField(max_length=1000, blank=True)
