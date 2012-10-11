from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from ventures.applications.forms import InfoForm
from ventures.applications.models import Application


def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you!')
        else:
            return render_to_response('applications/info_form.html',
                                      {'form': form},
                                      context_instance=RequestContext(request))
    else:
        form = InfoForm()
        return render_to_response('applications/info_form.html',
                                  {'form': form},
                                  context_instance=RequestContext(request))
