from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

from Core.control.HelperControl import PreparationBasicConfiguration

class Command(BaseCommand):
    help = "Scan i18n messages without going into externals."

    def handle(self, *args, **options):
        PreparationBasicConfiguration()
        print('System prepared successfully ... ')