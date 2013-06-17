from django.views import generic

from apps.rlogger.models import RequestLogger


class index(generic.ListView):

    template_name = 'rlogger/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        return RequestLogger.objects.all().order_by('created_on')[:10]
