from apps.rlogger.models import RequestLogger


class LoggerMiddleware(object):

    def process_request(self, request):
        logger_event = RequestLogger.objects.create(
            method=request.method, path=request.path)
        logger_event.save()
        return None
