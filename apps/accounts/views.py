try:
    import simplejson as json
except ImportError:
    from django.utils import simplejson as json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic

from .models import UserProfile
from .forms import UserProfileForm


class index(generic.ListView):

    template_name = 'accounts/index.html'
    context_object_name = 'profile'

    def get_queryset(self):
        if settings.HOSTING_PROVIDER == 'getbarista':
            try:
                return UserProfile.objects.get(id=1)
            except UserProfile.DoesNotExist:
                fix_getbarista_load_fixtures_from_app_bug()
            return UserProfile.objects.get(id=1)
        else:
            return UserProfile.objects.get(id=1)


@login_required(login_url='/accounts/login/')
def edit(request):

    errors = {}
    profile = UserProfile.objects.get(pk=1)

    if request.method == 'POST':
        interaction_fields = ['first_name', 'last_name', 'bio',
                              'date_of_birth', 'email', 'jid',
                              'skype_id', 'other_contacts',
                              'user_photo']
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # We do not need to update some fields
            # such as username, password, etc.
            f = form.save(commit=False)
            f.save(update_fields=interaction_fields)
            if request.is_ajax():
                return HttpResponse(json.dumps(
                    {
                        'errors': errors,
                        'success': True
                    }), content_type="application/json")
            else:
                return redirect(reverse('accounts:edit'))
        else:
            if request.is_ajax():
                errors = dict(form.errors.items())
                return HttpResponse(json.dumps(
                    {
                        'errors': errors,
                        'success': False
                    }), content_type="application/json")
            else:
                return redirect(reverse('accounts:edit'))
    else:
        form = UserProfileForm(instance=profile)
        return render(request, 'accounts/user_profile_edit.html',
                      {'form': form, 'profile': profile})


def fix_getbarista_load_fixtures_from_app_bug():
    u = UserProfile.objects.create_superuser('dustin',
                                             'asherepa@gmail.com',
                                             'testdata')
    u.save()
