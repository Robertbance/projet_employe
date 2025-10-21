from django.db import models

class Employe(models.Model):
    Choix_Sexe= [
        ('H', 'Homme'),
        ('F', 'Femme'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    poste = models.CharField(max_length=100)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    sexe = models.CharField(max_length=1, choices=Choix_Sexe, default='H')

    def __str__(self):
        return self.nom
