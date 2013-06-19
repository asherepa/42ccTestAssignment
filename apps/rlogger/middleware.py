from .models import RequestsLogger


class RequestsLoggerMiddleware(object):
    def process_request(self, request):
        logger_event = RequestsLogger.objects.create(
            method=request.method, path=request.path)
        logger_event.save()
        return None
