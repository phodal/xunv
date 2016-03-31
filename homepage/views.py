from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def index(request):
    context = { 'MAPBOX_ID': settings.MAPBOX_ID, 'MAPBOX_TOKEN': settings.MAPBOX_TOKEN}
    return render_to_response('index.html', context, context_instance=RequestContext(request))
