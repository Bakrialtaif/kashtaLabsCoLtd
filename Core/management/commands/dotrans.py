from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Scan i18n messages without going into externals."

    def handle(self, *args, **options):
        options['all'] = True
        options['extensions'] = ['html', 'inc', 'py']
        options['ignore_patterns'] = ['env*']
        call_command('makemessages', **options)