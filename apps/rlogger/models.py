from django.db import models


class RequestsLogger(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=254)
