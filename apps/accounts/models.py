from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.db import models


class UserProfile(AbstractUser):
    date_of_birth = models.DateField(default='1970-01-01')
    bio = models.TextField(max_length=1000, blank=True)
    jid = models.CharField(max_length=254, blank=True)
    skype_id = models.CharField(max_length=254, blank=True)
    other_contacts = models.TextField(max_length=1000, blank=True)
    user_photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                                   blank=True, null=True)


class ModelLog(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=10)
    event_info = models.CharField(max_length=255)


def ModelCreateUpdateHandler(sender, **kwargs):
    if sender._meta.module_name == 'modellog':
        return None
    try:
        if 'created' in kwargs:
            event_type = 'Create' if kwargs['created'] else 'Update'
        else:
            event_type = 'Delete'
        m = ModelLog.objects.create(event_type=event_type,
                                    event_info=kwargs['instance'])
        m.save()
    except:
        pass


post_save.connect(ModelCreateUpdateHandler)
post_delete.connect(ModelCreateUpdateHandler)
