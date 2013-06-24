from django import forms
from django.utils.safestring import mark_safe
from .models import UserProfile


class CalendarWidget(forms.DateInput):

    class Media:
        css = {
            'all': ('http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css',)
        }
        js = (
            'http://code.jquery.com/jquery-1.9.1.js',
            'http://code.jquery.com/ui/1.10.3/jquery-ui.js',
        )

    def __init__(self, params='', attrs=None):
        self.params = params
        super(CalendarWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(CalendarWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe('''<script type="text/javascript">
            $('#id_%s').datepicker({%s});
            </script>''' % (name, self.params))


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['username', 'password', 'last_login', 'date_joined',
                   'is_staff, is_active, is_superuser']
        widgets = {
            'user_photo': forms.widgets.FileInput(attrs={
                            'accept': "image/jpeg,image/png,image/gif",
                            'size': 11
                          }),
            'date_of_birth': CalendarWidget(params='''changeYear: true,
                    dateFormat: "yy-mm-dd", yearRange: "c-100:c+0",
                    maxDate: "+2D"''', attrs={'class': 'datepicker'}
                )
        }

    class Media:
        js = (
            'js/jquery.form.js',
            'js/accounts.js'
        )

    def clean_skype_id(self):
        skype_id = self.cleaned_data['skype_id']
        if len(skype_id) < 6 or len(skype_id) > 32:
            raise forms.ValidationError('Login length must be in the range of 6 to 32')
        return skype_id
