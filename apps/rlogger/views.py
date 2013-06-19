from django.views import generic
from .models import RequestsLogger


class index(generic.ListView):
    template_name = 'rlogger/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        return RequestsLogger.objects.order_by('created_on')[:10]
