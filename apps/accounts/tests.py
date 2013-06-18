from datetime import date
from django.test import TestCase
from django.test import Client
from apps.accounts.models import UserProfile
from .forms import UserProfileForm

USER_NAME = 'Andriy'
USER_NEW_NAME = 'King-Kong-Dong'
USER_SURNAME = 'Sherepa'
USER_DATE_OF_BIRTH = date(1986, 10, 30)
USER_BIO = "It's my life\r\nIt's now or never\r\nI ain't gonna live forever"\
    "\r\nI just want to live while I'm live\r\nIt's my life"
USER_JABBER_JID = 'dustin@jabber.ru'
USER_SKYPE_ID = 'a.sherepa'
USER_OTHER_CONTACTS = 'Location: Kiev\r\nPhone: +380675976116'


class SimpleTest(TestCase):

    def test_main_page_context_data(self):

        c = Client()
        response = c.get('/')
        profile = response.context['profile']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(profile.first_name, USER_NAME)
        self.assertEqual(profile.last_name, USER_SURNAME)
        self.assertEqual(profile.date_of_birth, USER_DATE_OF_BIRTH)
        self.assertEqual(profile.bio, USER_BIO)
        self.assertEqual(profile.jid, USER_JABBER_JID)
        self.assertEqual(profile.skype_id, USER_SKYPE_ID)
        self.assertEqual(profile.other_contacts, USER_OTHER_CONTACTS)


class AuthTest(TestCase):

    def test_login(self):
        c = Client()
        c.get('/accounts/login/')
        self.assertTrue(c.login(username='dustin',
                                password='testdata'))
        response = c.get('/accounts/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logout')

    def test_redirect_to_login_page_without_auth(self):
        c = Client()
        response = c.get('/accounts/edit/')
        self.assertEqual(response.status_code, 302)


class UserProfileFormTest(TestCase):

    def test_user_profile_form(self):
        """
        Login and submit new first_name value.
        Then try to read the updated data. Another data is still here.
        """
        data = {}
        interaction_field = ['first_name', 'last_name', 'bio', 'date_of_birth',
                             'email', 'jid', 'skype_id', 'other_contacts']
        profile = UserProfile.objects.get(id=1)
        for form_field in interaction_field:
            if hasattr(profile, form_field):
                data[form_field] = getattr(profile, form_field)
        data['first_name'] = USER_NEW_NAME
        f = UserProfileForm(data)
        self.assertTrue(f.is_valid())

        c = Client()
        c.get('/accounts/login/')
        c.login(username='dustin', password='testdata')
        response = c.post('/accounts/edit/', data)
        response = c.get(response['Location'])
        self.assertContains(response, USER_NEW_NAME)
        self.assertContains(response, USER_SURNAME)
