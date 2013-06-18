try:
    import simplejson as json
except ImportError:
    from django.utils import simplejson as json

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse

from .models import UserProfile
from .forms import UserProfileForm


def index(request):
    if request.user.is_authenticated():
        return redirect('edit')
    profile = UserProfile.objects.get(id=1)
    return render(request, 'accounts/index.html',
                  {'profile': profile})


@login_required
def edit(request):
    profile = UserProfile.objects.get(id=1)

    if request.is_ajax():  # only if AJAX
        if getattr(settings, 'DEBUG', False):  # only if DEBUG=True
            import time
            time.sleep(2)  # delay AJAX response for 5 seconds

    if request.method == 'POST':
        errors = {}
        interaction_field = ['first_name', 'last_name', 'bio', 'date_of_birth',
                             'email', 'jid', 'skype_id', 'other_contacts',
                             'user_photo']
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            f = form.save(commit=False)
            f.save(update_fields=interaction_field)
            if request.is_ajax():
                return HttpResponse(json.dumps({'errors': errors,
                                                'success': True}))
            else:
                return redirect('/accounts/edit/')
        else:
            if request.is_ajax():
                errors = dict(form.errors.items())
                return HttpResponse(json.dumps({'errors': errors,
                                                'success': False}))
            else:
                return redirect('/accounts/edit/')
    else:
        form = UserProfileForm(instance=profile)
        return render(request, 'accounts/index.html',
                      {'profile': profile, 'form': form})
