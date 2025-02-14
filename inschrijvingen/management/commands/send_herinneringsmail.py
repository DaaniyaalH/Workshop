from django.core.management.base import BaseCommand
from inschrijvingen.tasks import send_herinneringsmail

class Command(BaseCommand):
    help = 'Verstuurt herinneringsmails voor workshops die binnen 2 dagen plaatsvinden'

    def handle(self, *args, **kwargs):
        send_herinneringsmail()
        self.stdout.write(self.style.SUCCESS('Herinneringsmails zijn succesvol verstuurd.'))
