from django import forms
from .models import UserProfile


class CalendarWidget(forms.DateInput):

    class Media:
        css = {
            'all': ("http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css",)
        }


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['username', 'password', 'last_login', 'date_joined']
        widgets = {
            'bio': forms.widgets.Textarea(attrs={'cols': 40, 'rows': 8}),
            'other_contacts': forms.widgets.Textarea(attrs={'cols': 40, 'rows': 8}),
            'user_photo': forms.widgets.FileInput(attrs={
                            'accept': "image/jpeg,image/png,image/gif",
                            'size': 11
                          }),
            'date_of_birth': CalendarWidget(attrs={'id': 'datepicker'}),
        }

    class Media:
        js = ('http://code.jquery.com/jquery-1.9.1.js',
              'http://code.jquery.com/ui/1.10.3/jquery-ui.js',
              'js/jquery.form.js',
              'js/accounts.js'
        )
