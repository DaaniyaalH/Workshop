from django.shortcuts import render, redirect, get_object_or_404
from .forms import InschrijvingForm
from .models import Inschrijving, Workshop
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# 🔹 Lijst van workshops
def workshop_list(request):
    workshops = Workshop.objects.all()
    return render(request, 'inschrijvingen/workshop_list.html', {'workshops': workshops})

# 🔹 Detailpagina van een specifieke workshop
def workshop_detail(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)
    return render(request, 'inschrijvingen/workshop_detail.html', {'workshop': workshop})

# 🔹 Bevestigingspagina
def inschrijving_bevestiging_view(request):
    return render(request, 'inschrijvingen/inschrijving_bevestiging.html')


# 🔹 Functie om bevestigingsmail te sturen
def stuur_bevestigingsmail(user_email, workshop):
    # Haal gegevens voor de email
    subject = 'Bevestiging van je inschrijving'
    message = render_to_string('inschrijvingen/bevestigingsmail_template.html', {
        'gebruiker_naam': user_email.split('@')[0],  # Gebruik de naam uit het emailadres
        'workshop_title': workshop.title,
        'workshop_location': workshop.location,
        'workshop_date': workshop.date,
    })
    plain_message = strip_tags(message)  # Maak een tekstversie van de email
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,  # Dit is je e-mailadres in settings.py
        [user_email],  # Verzenden naar het emailadres van de gebruiker
        html_message=message,
    )


# 🔹 Functie voor inschrijven
def inschrijving_view(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)

    if request.method == 'POST':
        form = InschrijvingForm(request.POST)
        if form.is_valid():
            # Controleer of de gebruiker al is ingeschreven
            bestaande_inschrijving = Inschrijving.objects.filter(
                email=form.cleaned_data['email'], 
                workshop=workshop
            ).exists()

            if bestaande_inschrijving:
                messages.error(request, "Je bent al ingeschreven voor deze workshop.")
                return redirect('workshop_detail', workshop_id=workshop.id)

            # Opslaan als inschrijving nog niet bestaat
            inschrijving = form.save(commit=False)
            inschrijving.workshop = workshop
            inschrijving.save()

            # Stuur bevestigingsmail
            stuur_bevestigingsmail(form.cleaned_data['email'], workshop)

            messages.success(request, "Je inschrijving is succesvol!")
            return redirect('inschrijving_bevestiging')  

    else:
        form = InschrijvingForm()

    return render(request, 'inschrijvingen/workshop_detail.html', {'form': form, 'workshop': workshop})
