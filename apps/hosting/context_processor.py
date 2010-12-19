from django.conf import settings
from models import Host

def featured(request):
    '''
        A context processor to add a list of featured hosts 
    '''
    hosts = Host.objects.filter(approved=True).order_by('?')[:5]
    return {
        'featured_hosts': hosts,
    }
