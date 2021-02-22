from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

from Core.control.DatabaseController import DatabaseController

class Command(BaseCommand):
    help = "Scan i18n messages without going into externals."

    def handle(self, *args, **options):
        DatabaseController().prepare_db_ideoms_to_in_translation_file()
        print('translatable ideoms updated successfully ... ')
        options['all'] = True
        options['extensions'] = ['html', 'inc', 'py']
        options['ignore_patterns'] = ['b-env*']
        call_command('makemessages', **options)