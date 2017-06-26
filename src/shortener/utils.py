import random
import string 
from django.conf import settings 

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 8)

def code_generator(size=SHORTCODE_MIN, chars_to_choose=string.ascii_lowercase  + string.digits):
	shortcode = ''
	for _ in range(size):
		shortcode += random.choice(chars_to_choose)
	return shortcode

def create_shortcut(instance, size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	Klass = instance.__class__
	exists = Klass.objects.filter(shortcodeurl=new_code).exists()
	if exists:
		return create_shortcut(size)
	return new_code