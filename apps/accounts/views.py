from django.views import generic

from apps.accounts.models import UserProfile


class index(generic.ListView):

    template_name = 'accounts/index.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return UserProfile.objects.get(id=1)
