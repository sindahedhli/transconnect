from django.db import models
from EntreprisesApp.models import Entreprise


class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20, null=False, blank=False, unique=True)
    type_vehicule = models.CharField(max_length=100, choices=[
        ('camionnette', 'Camionnette'),
        ('fourgon', 'Fourgon'),
        ('camion_porteur', 'Camion porteur'),
        ('semi_remorque', 'Semi-remorque'),
    ])
    capacite_kg = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.immatriculation