from django import forms
from .models import UserProfile


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
                          })
        }
