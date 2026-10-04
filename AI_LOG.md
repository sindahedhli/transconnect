\- Outil IA utilisé : Claude

\- Prompt : "Écris les modèles Django pour TransConnect selon le diagramme de classe fourni"

\- Sortie obtenue (résumé) : modèles Utilisateur, Entreprise, Vehicule, Expedition, Offre générés

\- Écarts identifiés vs cahier des charges (modèle Offre, exercice IV du document) :

&#x20; 1. prix en CharField au lieu de DecimalField

&#x20; 2. delai\_jours en IntegerField au lieu de PositiveIntegerField

&#x20; 3. date\_proposition avec auto\_now au lieu de auto\_now\_add

&#x20; 4. vehicule avec on\_delete=CASCADE incohérent avec null=True (doit être SET\_NULL)

\- Correction apportée et justification : voir commit "Review:" ci-dessous

