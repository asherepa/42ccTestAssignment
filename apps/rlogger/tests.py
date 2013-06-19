from django.test import TestCase
from .models import RequestsLogger

REQUESTS_PAGE_URL = '/requests/'
REQUESTS_PAGE_MAX_RECORD_PER_PAGE = 10


class RequestsPageTest(TestCase):
    def test_record_created_in_db(self):
        count_before = RequestsLogger.objects.count()
        self.client.get('/')
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
