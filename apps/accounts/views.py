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
    if request.method == 'POST':
        profile = UserProfile.objects.get(id=1)
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
        initial_form_data = {}
        profile = UserProfile.objects.get(id=1)
        for el in profile._meta.get_all_field_names():
            if hasattr(profile, el):
                initial_form_data[el] = getattr(profile, el)
        form = UserProfileForm(initial=initial_form_data)
        return render(request, 'accounts/index.html',
                      {'profile': profile, 'form': form})
