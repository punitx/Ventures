from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from ventures.volunteers.forms import InfoForm
from ventures.volunteers.models import Volunteer


def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Thank you!')
    else:
        form = InfoForm()
        return render_to_response('volunteers/info_form.html', {'form': form},
                                  context_instance=RequestContext(request))
