from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from ventures.resources.forms import ResourceForm
from ventures.resources.models import Resource


def index(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you!')
        else:
            return render_to_response('resources/resource_form.html',
                                      {'form': form},
                                      context_instance=RequestContext(request))
    else:
        form = ResourceForm()
        return render_to_response('resources/resource_form.html',
                                  {'form': form},
                                  context_instance=RequestContext(request))
