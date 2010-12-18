from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from models import Host

def index(request):
    template_name = 'base.html'
    context = RequestContext(request)
    dict = {}
    dict['hosts'] = Host.objects.filter(approved=True).order_by('type')
    dict['featured'] = Host.objects.filter(approved=True, featured=True)
    return render_to_response(
        template_name,
        dict,
        context,
    )

def view_host(request, host_slug):
    template_name = 'about.html'
    context = RequestContext(request)
    dict = {}
    host = Host.objects.get(slug=host_slug)
    return render_to_response(
        template_name,
        dict,
        context,
    )

def about(request):
    template_name = 'about.html'
    context = RequestContext(request)
    dict = {}
    return render_to_response(
        template_name,
        dict,
        context,
    )

def contact(request):
    template_name = 'base.html'
    context = RequestContext(request)
    dict = {}
    return render_to_response(
        template_name,
        dict,
        context,
    )
