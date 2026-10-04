from django.db import models
from django.contrib.auth.models import AbstractUser


class Utilisateur(AbstractUser):
    user_id = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    role = models.CharField(max_length=20, choices=[
        ('chargeur', 'Chargeur'),
        ('transporteur', 'Transporteur'),
        ('admin', 'Administrateur'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200, null=False, blank=False)
    matricule_fiscal = models.CharField(max_length=17, null=False, blank=False, unique=True)
    adresse = models.TextField()
    type_entreprise = models.CharField(max_length=100, choices=[
        ('chargeur', 'Chargeur'),
        ('transporteur', 'Transporteur'),
    ])
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.raison_sociale