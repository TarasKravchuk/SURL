from shortener.models import ShortSURL
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Refrehes all ShortURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items ', type=int)

    def handle(self, *args, **options):
        return ShortSURL.objects.refresh_shortcodes(items=['items'])
