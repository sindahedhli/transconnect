from django.db import models
from ExpeditionsApp.models import Expedition
from EntreprisesApp.models import Entreprise
from VehiculesApp.models import Vehicule


class Offre(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    delai_jours = models.PositiveIntegerField()
    statut = models.CharField(max_length=20, choices=[
        ('proposee', 'Proposée'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
        ('retiree', 'Retirée'),
    ], default='proposee')
    date_proposition = models.DateField(auto_now_add=True)
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
    transporteur = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Offre {self.id} - {self.expedition.reference}"