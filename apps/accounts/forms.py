from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['username', 'password', 'last_login', 'date_joined',
                   'is_staff, is_active, is_superuser']
        widgets = {
            'user_photo': forms.widgets.FileInput(attrs={
                            'accept': "image/jpeg,image/png,image/gif",
                            'size': 11
                        })
        }

    def clean_skype_id(self):
        skype_id = self.cleaned_data['skype_id']
        if len(skype_id) < 6 or len(skype_id) > 32:
            raise forms.ValidationError('Login length must be in the range of 6 to 32')
        return skype_id
