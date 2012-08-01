from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from polls.models import Poll, Choice
from polls.forms import PollForm


def index(request):
    latest_poll_list = Poll.published.all().order_by('-pub_date')[:5]
    print latest_poll_list;
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
    p = get_object_or_404(Poll.published.all(), pk=poll_id)

    if request.method == 'POST':
        form = PollForm(request.POST, instance=p)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls_results', kwargs={'poll_id': p.id}))
    else:
        form = PollForm(instance=p)

    return render_to_response('polls/detail.html', {
        'poll': p,
        'form': form,
    }, context_instance=RequestContext(request))


def results(request, poll_id):
    p = get_object_or_404(Poll.published.all(), pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})
