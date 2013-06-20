from datetime import date
from django.core.urlresolvers import reverse
from django.test import TestCase


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

        response = self.client.get(reverse('accounts:index'))
        profile = response.context['profile']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(profile.first_name, USER_NAME)
        self.assertEqual(profile.last_name, USER_SURNAME)
        self.assertEqual(profile.date_of_birth, USER_DATE_OF_BIRTH)
        self.assertEqual(profile.bio, USER_BIO)
        self.assertEqual(profile.jid, USER_JABBER_JID)
        self.assertEqual(profile.skype_id, USER_SKYPE_ID)
        self.assertEqual(profile.other_contacts, USER_OTHER_CONTACTS)
