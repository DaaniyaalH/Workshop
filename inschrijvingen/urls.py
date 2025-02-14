from django.urls import path
from . import views
from .views import workshop_list, workshop_detail, inschrijving_view, inschrijving_bevestiging_view
urlpatterns = [
    # Lijst van workshops bekijken
    path('workshops/', views.workshop_list, name='workshop_list'),

    # Workshop detailpagina + inschrijven
    path('workshops/<int:workshop_id>/', views.workshop_detail, name='workshop_detail'),

    # Inschrijving voor een specifieke workshop
    path('workshops/<int:workshop_id>/inschrijven/', views.inschrijving_view, name='inschrijving'),

    # Bevestigingspagina
    path('inschrijving/bevestiging/', views.inschrijving_bevestiging_view, name='inschrijving_bevestiging'),
]
