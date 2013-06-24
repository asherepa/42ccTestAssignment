from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import RequestsLogger


def index(request):
    template_name = 'rlogger/index.html'

    sort_order = request.GET.get('sort', '0')
    reverse_mode = request.GET.get('mode', '0')
    if reverse_mode == '1':
        sort_order = '1' if sort_order == '0' else '0'
    if sort_order == '1':
        events = RequestsLogger.objects.order_by('priority', 'created_on')[:10]
    else:
        events = RequestsLogger.objects.order_by('-priority', 'created_on')[:10]
    context = {'events': events, 'sort_order': sort_order}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def event(request, event_id):
    event = get_object_or_404(RequestsLogger, pk=event_id)
    action = request.GET['action']
    sort_order = request.GET['sort']
    if action == 'up':
        event.priority += 1
    elif action == 'down':
            event.priority -= 1
    event.save()
    url = '%s?sort=%s' % (reverse('requests:index'), sort_order)
    return HttpResponseRedirect(url)
