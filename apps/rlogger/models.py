from django.db import models


class RequestsLogger(models.Model):
    PRIORITY_CHOICES = (
        (0, 'Priority 0'),
        (1, 'Priority 1'),
    )
    created_on = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=254)
    priority = models.IntegerField(choices=PRIORITY_CHOICES,
                                   default=0)

    def __unicode__(self):
        return "%s %s (%d)" % (self.method, self.path, self.priority)
