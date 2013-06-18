from django.views import generic
from django.conf import settings

from apps.accounts.models import UserProfile


class index(generic.ListView):

    template_name = 'accounts/index.html'
    context_object_name = 'profile'

    def get_queryset(self):
        print settings.HOSTING_PROVIDER
        if settings.HOSTING_PROVIDER == 'getbarista':
            try:
                return UserProfile.objects.get(id=1)
            except UserProfile.DoesNotExist:
                fix_getbarista_load_fixtures_from_app_bug()
            return UserProfile.objects.get(id=1)
        else:
            return UserProfile.objects.get(id=1)


def fix_getbarista_load_fixtures_from_app_bug():
    u = UserProfile.objects.create_superuser('dustin',
                                             'asherepa@gmail.com',
                                             'testdata')
    u.save()
    print u
