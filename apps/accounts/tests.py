from datetime import date, datetime
try:
    import simplejson as json
except ImportError:
    from django.utils import simplejson as json
import os
import StringIO

from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.template import Context, Template
from django.test import TestCase
from .forms import UserProfileForm
from .models import UserProfile, ModelLog

USER_NAME = 'Andriy'
USER_LOGIN = 'admin'
USER_PASSWORD = 'admin'
USER_NEW_NAME = 'King-Kong-Dong'
USER_SURNAME = 'Sherepa'
USER_EMAIL = 'a.sherepa@gmail.com'
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

    def test_simple_login(self):
        self.assertTrue(self.client.login(username=USER_LOGIN,
                                          password=USER_PASSWORD))

    def test_login_and_logout_success(self):

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

    def setUp(self):

        self.valid_data = {
            'first_name': USER_NAME,
            'last_name': USER_SURNAME,
            'bio': USER_BIO,
            'date_of_birth': USER_DATE_OF_BIRTH,
            'email': USER_EMAIL,
            'jid': USER_JABBER_JID,
            'skype_id': USER_SKYPE_ID,
            'other_contacts': USER_OTHER_CONTACTS
        }

        self.invalid_data_set = [
            {'skype_id': 'error'},  # len < 6
        ]
        self.assertTrue(self.client.login(username=USER_LOGIN,
                                          password=USER_PASSWORD))

    def test_user_profile_form(self):

        form = UserProfileForm(self.valid_data)
        self.assertTrue(form.is_valid())

        with open('assets/img/empty.png') as fphoto:
            self.valid_data['user_photo'] = fphoto
            form = UserProfileForm(self.valid_data)
            self.assertTrue(form.is_valid())

        for data in self.invalid_data_set:
                for key, value in data.iteritems():
                    invalid_data = self.valid_data
                    invalid_data[key] = value
                    form = UserProfileForm(invalid_data)
                    self.assertFalse(form.is_valid())

    def test_ajax_form_update_with_correct_data(self):

        returned_data = self.post_request(self.valid_data)
        self.assertTrue(returned_data['success'])
        self.assertEqual(returned_data['errors'], {})

    def test_ajax_form_update_with_bad_data(self):

        for data in self.invalid_data_set:
                for key, value in data.iteritems():
                    invalid_data = self.valid_data
                    invalid_data[key] = value
                    returned_data = self.post_request(invalid_data)
                    self.assertFalse(returned_data['success'])
                    errors = returned_data['errors']
                    self.assertTrue(key in errors)

    def post_request(self, data):

        response = self.client.post(
            reverse('accounts:edit'),
            self.valid_data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response['Content-Type'],
                        'application/json')
        returned_data = json.loads(response.content)
        self.assertTrue('success' in returned_data)
        self.assertTrue('errors' in returned_data)
        return returned_data


class TemplateTagTest(TestCase):

    def test_edit_link_template_tag(self):
        self.assertTrue(self.client.login(username=USER_LOGIN,
                                          password=USER_PASSWORD))
        response = self.client.get(APP_MAIN_PAGE)
        context = response.context
        t = Template('{% load edit_tags %}' +
                     '{% edit_link user %}')
        c = Context(context)
        rendered = t.render(c)
        self.assertEqual(rendered, "/admin/accounts/userprofile/1/")


class CommandCountTest(TestCase):

    def test_command_count(self):
        f = StringIO.StringIO()
        call_command('count', stdout=f)
        l = f.getvalue()
        self.assertTrue('Models accounts: 1\n' in l)
        self.assertFalse('Models accounts: 2\n' in l)


class SignalsTest(TestCase):

    def test_create_signal(self):
        before_count = ModelLog.objects.count()
        u = UserProfile.objects.create(username='test',
                                       email='test@example.com',
                                       password='testpassword')
        after_count = ModelLog.objects.count()
        self.assertEqual(after_count, before_count + 1)
        before_count = after_count
        u.username = 'another'
        u.save()
        after_count = ModelLog.objects.count()
        self.assertEqual(after_count, before_count + 1)
        u.delete()
