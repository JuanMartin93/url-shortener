
from django.db import models
from django.conf import settings

# Create your models here.

from .utils import code_generator, create_shortcut
from .validators import validate_url, validate_dot_com
from django_hosts.resolvers import reverse


SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 20)

class KUrlManager(models.Manager):
	def all(self, *args, **kwargs):
		original = super(KUrlManager, self). all(*args, **kwargs)
		new = original.filter(active=True)
		return new

	def refresh_objects_shortcode(self, items=None):
		print(items)
		objects = KUrl.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			objects = objects.order_by('-url')[:items]
		new_codes=0
		for q in objects:
			q.shortcodeurl = create_shortcut(q)
			q.save()
			new_codes += 1
		return "New codes: {i} " .format(i=new_codes)



class KUrl (models.Model):
	url = models.CharField(max_length=200 , validators=[validate_url, validate_dot_com])
	shortcodeurl = models.CharField(max_length = SHORTCODE_MAX, unique=True, blank=True)
	updated_date = models.DateField(auto_now =True)
	timestamp = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=True)
	objects = KUrlManager()


	def save(self, *args, **kwargs):
		if self.shortcodeurl is None or self.shortcodeurl == "":
			self.shortcodeurl = create_shortcut(self)
		super(KUrl, self).save(*args, **kwargs) 

	def __str__(self):
		return str(self.url)

	def __unicode__ (self):
		return str(self.url)

	def get_short_url(self):
		url_path = reverse("scode", kwargs={'shortcode':self.shortcodeurl}, host='www',scheme='http')
		return url_path

