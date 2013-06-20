from datetime import date
from django.core.urlresolvers import reverse
from django.test import TestCase
from .forms import UserProfileForm


USER_NAME = 'Andriy'
USER_LOGIN = 'dustin'
USER_PASSWORD = 'testdata'
USER_NEW_NAME = 'King-Kong-Dong'
USER_SURNAME = 'Sherepa'
USER_EMAIL = 'asherepa@gmail.com'
USER_DATE_OF_BIRTH = date(1986, 10, 30)
USER_BIO = "It's my life\r\nIt's now or never\r\nI ain't gonna live forever"\
    "\r\nI just want to live while I'm live\r\nIt's my life"
USER_JABBER_JID = 'dustin@jabber.ru'
USER_SKYPE_ID = 'a.sherepa'
USER_OTHER_CONTACTS = 'Location: Kiev\r\nPhone: +380675000006'
APP_MAIN_PAGE = reverse('accounts:index')


class SimpleTest(TestCase):
    def test_main_page_context_data(self):
        response = self.client.get(APP_MAIN_PAGE)
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
    def test_login_success(self):
        response = self.client.get(APP_MAIN_PAGE)
        self.assertTrue(response.status_code, 200)
        self.assertTrue(self.client.login(username=USER_LOGIN,
                                          password=USER_PASSWORD))
        response = self.client.get(reverse('accounts:edit'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logout')
        self.client.logout()
        response = self.client.get(reverse('accounts:edit'))
        self.assertEqual(response.status_code, 302)

    def test_unauth_request_edit_page(self):
        response = self.client.get(APP_MAIN_PAGE)
        self.assertContains(response, 'Login')
        response = self.client.get(reverse('accounts:edit'))
        self.assertRedirects(response,
                             '/accounts/login/?next=/accounts/edit/')


class UserProfileFormTest(TestCase):

    valid_data = {
        'first_name': USER_NAME,
        'last_name': USER_SURNAME,
        'bio': USER_BIO,
        'date_of_birth': USER_DATE_OF_BIRTH,
        'email': USER_EMAIL,
        'jid': USER_JABBER_JID,
        'skype_id': USER_SKYPE_ID,
        'other_contacts': USER_OTHER_CONTACTS
    }

    invalid_data_set = [
        {'skype_id': 'error'},  # len < 6
    ]

    def test_user_profile_form(self):
        form = UserProfileForm(self.valid_data)
        self.assertTrue(form.is_valid())

        with open('assets/img/empty.png') as fphoto:
            self.valid_data['user_photo'] = fphoto
            self.assertTrue(form.is_valid())

        for data in self.invalid_data_set:
                for key, value in data.iteritems():
                    check_data = self.valid_data
                    check_data[key] = value
                    form = UserProfileForm(check_data)
                    self.assertFalse(form.is_valid())
