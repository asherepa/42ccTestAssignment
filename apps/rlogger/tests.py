from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import RequestsLogger

USER_LOGIN = 'admin'
USER_PASSWORD = 'admin'
REQUESTS_PAGE_MAX_RECORD_PER_PAGE = 10
REQUESTS_PAGE_URL = reverse('requests:index')


class RequestsPageTest(TestCase):
    def test_record_created_in_db(self):
        count_before = RequestsLogger.objects.count()
        self.client.get(reverse('accounts:index'))
        count_after = RequestsLogger.objects.count()
        self.assertEqual(count_after, count_before + 1)

    def test_add_record_count(self):
        """
        Checking a new record created after the opening some pages
        """
        count_before = self.get_response_count()
        self.assertEqual(self.get_response_count(),
                         count_before + 1)

    def test_requests_page_max_record_per_page(self):
        for i in xrange(1, 12):
            self.client.get(REQUESTS_PAGE_URL)
        self.assertEqual(self.get_response_count(),
                         REQUESTS_PAGE_MAX_RECORD_PER_PAGE)

    def get_response_count(self):
        response = self.client.get(REQUESTS_PAGE_URL)
        events_list = response.context['events']
        return events_list.count()


class ContextProcessorTest(TestCase):
    def test_settings_context_processor(self):
        response = self.client.get(reverse('accounts:index'))
        self.assertTrue('settings' in response.context)
        settings_context = response.context['settings']
        self.assertEqual(settings_context.AUTH_USER_MODEL,
                         'accounts.UserProfile')


class ChangePriorityTest(TestCase):

    def test_change_priority(self):
        self.assertTrue(self.client.login(username=USER_LOGIN,
                                          password=USER_PASSWORD))
        self.client.get(reverse('requests:index'))
        r = RequestsLogger.objects.get(pk=1)
        self.assertEqual(r.priority, 0)

        url = "%s?sort=0&action=up" % reverse('requests:event', args=(r.id,))
        self.assertEqual(self.check_update(url, r.id), 1)

        url = "%s?sort=0&action=down" % reverse('requests:event', args=(r.id,))
        self.assertEqual(self.check_update(url, r.id), 0)

    def check_update(self, url, key):
        self.client.get(url)
        r = RequestsLogger.objects.get(pk=key)
        return r.priority
