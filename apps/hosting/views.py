from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from models import Host
from forms import HostForm

def index(request):
    template_name = 'base.html'
    context = RequestContext(request)
    dict = {}
    dict['hosts'] = Host.objects.filter(approved=True).order_by('type')
    dict['featured'] = Host.objects.random(featured=True)
    dict['featured_hosts'] = Host.objects.filter(approved=True, featured=True)
    return render_to_response(
        template_name,
        dict,
        context,
    )

def view_host(request, host_slug):
    template_name = 'host.html'
    context = RequestContext(request)
    dict = {}
    host = Host.objects.get(slug=host_slug)
    dict['host'] = host
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

def add(request):
    template_name = 'add.html'
    context = RequestContext(request)
    dict = {}
    if request.POST:
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            dict['message'] = "Thank you for add a new host. We'll review it as quickly as we can and add it to the site"
            form = HostForm()
    else:
        form = HostForm()    

    dict['form'] = form    
    return render_to_response(
        template_name,
        dict,
        context,
    )
