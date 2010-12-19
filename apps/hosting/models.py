import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from random import randint
from django.db.models import Count

class HostType(models.Model):
    name = models.CharField(_('Host Type'), max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

def get_image_path(instance, filename):
    return os.path.join('host_images', str(instance.name), filename)

class UsersManager(models.Manager):
    def random(self, featured=False):
        if featured:
            count = self.filter(approved=True, featured=True).aggregate(count=Count('id'))['count']
        else:
            count = self.filter(approved=True).aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        if featured:
            return self.filter(approved=True, featured=True)[random_index]
        else:
            return self.filter(approved=True)[random_index]
	
class Host(models.Model):
    objects = UsersManager()
    name = models.CharField(_('Host Name'), max_length=100)
    slug = models.SlugField(unique=True)
    url = models.URLField(_('Host Website'))
    referral_url = models.URLField(_('Referral URL'), blank=True, null=True)
    type = models.ForeignKey(HostType)
    description = models.TextField()
    large_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    small_image_one = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    small_image_two = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    featured = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('name', 'url'),)
    def save(self, *args, **kwargs):
        if not self.id:
            count = Host.objects.filter(slug = slugify(self.name)).count()
            self.slug = slugify(self.name)
            if count > 0:
                count = Host.objects.all().count()
                self.slug = '%s_%s' % (self.slug, count)
        super(Host, self).save(*args, **kwargs)

    def get_url(self):
        if self.referral_url:
            return self.referral_url
        else:
            return self.url

    def __unicode__(self):
        return self.name
