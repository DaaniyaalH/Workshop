from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Inschrijving

def send_herinneringsmail():
    # 2 dagen voor de workshopdatum
    herinnering_date = timezone.now() + timedelta(days=2)
    
    # Zoek alle inschrijvingen waarvan de workshop binnenkort is
    inschrijvingen = Inschrijving.objects.filter(workshop__date__lte=herinnering_date)
    
    for inschrijving in inschrijvingen:
        workshop = inschrijving.workshop

        # Controleer of het emailadres aanwezig is in de inschrijving
        if inschrijving.email:
            # Stel onderwerp en bericht op voor de herinneringsmail
            subject = f"Herinnering: Je bent ingeschreven voor {workshop.title}"
            message = render_to_string('inschrijvingen/herinneringsmail_email.html', {
                'email': inschrijving.email,  # Gebruik het e-mailadres van de inschrijving
                'workshop': workshop,
            })

            # Verstuur de herinneringsmail
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [inschrijving.email],  # Gebruik het emailadres van de inschrijving
                fail_silently=False,
            )
        else:
            print(f"Geen geldig e-mailadres voor inschrijving {inschrijving.id}.")
