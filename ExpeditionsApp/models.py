import uuid
from django.db import models
from EntreprisesApp.models import Entreprise


class Expedition(models.Model):
    reference = models.CharField(max_length=20, unique=True, editable=False)
    ville_depart = models.CharField(max_length=100, null=False, blank=False)
    ville_arrivee = models.CharField(max_length=100, null=False, blank=False)
    poids_kg = models.DecimalField(max_digits=10, decimal_places=2)
    date_souhaitee = models.DateField()
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=[
        ('publiee', 'Publiée'),
        ('attribuee', 'Attribuée'),
        ('en_cours', 'En cours'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ], default='publiee')
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = f"EXP-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference