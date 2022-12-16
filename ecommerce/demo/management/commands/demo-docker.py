from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self):
        call_command('docker-compose --profile dev up -d')
        