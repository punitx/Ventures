from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from ventures.judges.forms import InfoForm
from ventures.judges.models import Judge


def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you!')
        else:
            return render_to_response('judges/info_form.html', {'form': form},
                                      context_instance=RequestContext(request))
    else:
        form = InfoForm()
        return render_to_response('judges/info_form.html', {'form': form},
                                  context_instance=RequestContext(request))
