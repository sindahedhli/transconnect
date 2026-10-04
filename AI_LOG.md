\- Outil IA utilisé : Claude

\- Prompt : "Écris les modèles Django pour TransConnect selon le diagramme de classe fourni"

\- Sortie obtenue (résumé) : modèles Utilisateur, Entreprise, Vehicule, Expedition, Offre générés

\- Écarts identifiés vs cahier des charges (modèle Offre, exercice IV du document) :

 1. prix en CharField au lieu de DecimalField
Correction : DecimalField(max_digits=10, decimal_places=2)

2. delai_jours = models.IntegerField()
IntegerField accepte les valeurs négatives. Un délai de livraison en jours n'a pas de sens négatif. Correction : PositiveIntegerField()
 3. date_proposition = models.DateField(auto_now=True)
C'est la plus subtile. auto_now=True réécrit la date à chaque fois que l'objet est sauvegardé, pas seulement à la création. Si un transporteur modifie plus tard le statut de son offre (proposee → acceptee), la date de proposition serait faussement mise à jour à cette date-là, alors qu'elle doit rester figée à la date de la proposition initiale. Correction : auto_now_add=True (ne s'applique qu'une seule fois, à la création).
 4. vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, null=True)
Contradiction logique : null=True dit "cette offre peut exister sans véhicule renseigné", mais on_delete=CASCADE dit "si le véhicule est supprimé, supprime l'offre avec lui" — ce qui va à l'encontre de l'idée qu'une offre puisse survivre sans véhicule. Correction : on_delete=models.SET_NULL (le véhicule disparaît, l'offre reste, le champ devient NULL).

- Remarque complémentaire sur la méthode save() du code fourni :
  La méthode save() présente dans le code source de l'exercice
  (def save(self, *args, **kwargs): super().save(*args, **kwargs))
  ne fait rien de plus que le comportement par défaut de Django : elle appelle
  simplement super().save() sans ajouter aucun traitement avant ou après.
  Supprimer cette méthode ne change donc rien au fonctionnement du modèle.
  Elle n'a pas été comptée parmi les 4 anomalies car elle ne casse aucune
  donnée, mais elle a été retirée du modèle final car inutile. À titre de
  comparaison, le save() du modèle Expedition, lui, a été conservé car il
  génère automatiquement le champ reference avant l'enregistrement, ce qui
  justifie sa présence.
\- Correction apportée et justification : voir commit "Review:" ci-dessous

