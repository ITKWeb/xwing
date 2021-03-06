from django.db import models

# Create your models here.

class Boite(models.Model):
    nom = models.CharField(max_length=50)
    image = models.CharField(max_length=50)


class Carte(models.Model):
    nom = models.CharField(max_length=50)
    points = models.IntegerField()
    boite = models.ForeignKey(Boite)

class Amelioration(Carte):
    AMELIORATION_CHOICES = (
        ('TP', 'Torpille'),
        ('DR', 'Droide'),
        ('TR', 'Tourelle'),
        ('MD', 'Medailles'),
        ('MS', 'Missiles'),
    )
    type_amelioration = models.CharField(max_length=2, choices=AMELIORATION_CHOICES)
              
class Vaisseau(models.Model):
    VAISSEAU_CHOICES = (
        ('XW', 'XWing'),
        ('YW', 'YWing'),
        ('TF', 'Chasseau TIE'),
        ('TA', 'TIE Advance'),
    )
    type_vaisseau = models.CharField(max_length=2, choices=VAISSEAU_CHOICES)

class Pilote(Carte):
    Camp_CHOICES = (
        ('E', 'Empire'),
        ('R', 'Rebelles'),
    )
    camp = models.CharField(max_length=2, choices=Camp_CHOICES)
    type_vaisseau = models.ForeignKey(Vaisseau)

class Ameliorations_Pilote(Carte):
     pilote =  models.ForeignKey(Pilote)
     nombre = models.IntegerField()
     type_amelioration = models.ForeignKey(Amelioration)

