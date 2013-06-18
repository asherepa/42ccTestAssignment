from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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
    if request.method == 'POST':
        interaction_field = ['first_name', 'last_name', 'bio', 'date_of_birth',
                             'email', 'jid', 'skype_id', 'other_contacts',
                             'user_photo']
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            f = form.save(commit=False)
            f.save(update_fields=interaction_field)
            return redirect('/accounts/edit/')
        else:
            return redirect('/accounts/edit/')
    else:
        form = UserProfileForm(instance=profile)
        return render(request, 'accounts/index.html',
                      {'profile': profile, 'form': form})
