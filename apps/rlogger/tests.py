from django.test import TestCase
from django.test import Client

REQUEST_PAGE_MAX_EVENTS = 10


class SimpleTest(TestCase):

    def test_request_page(self):
        c = Client()
        response = c.get('/request/')
        events_list = response.context['events']
        first_request_count = events_list.count()
        response = c.get('/request/')
        events_list = response.context['events']
        self.assertEqual(events_list.count(),
            first_request_count + 1)

    def test_request_page_max_entry(self):
        c = Client()
        for i in xrange(1, 12):
            response = c.get('/request/')
        events_list = response.context['events']
        self.assertEqual(events_list.count(),
            REQUEST_PAGE_MAX_EVENTS)
