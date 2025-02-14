from rest_framework import serializers
from .models import Inschrijving

class InschrijvingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inschrijving
        fields = ['user', 'workshop']
    
    def validate(self, data):
        # Validatie voor dubbele inschrijving
        if Inschrijving.objects.filter(user=data['user'], workshop=data['workshop']).exists():
            raise serializers.ValidationError("Je bent al ingeschreven voor deze workshop.")
        
        # Controleer of er voldoende capaciteit is voor de workshop
        if data['workshop'].capacity <= Inschrijving.objects.filter(workshop=data['workshop']).count():
            raise serializers.ValidationError("De workshop is vol.")
        
        return data
