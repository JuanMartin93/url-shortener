from django.core.management.base import BaseCommand, CommandError
from shortener.models import KUrl

class Command(BaseCommand):
    help = 'Changing the shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)



    def handle(self, *args, **options):
        return KUrl.objects.refresh_objects_shortcode(items=options['items'])