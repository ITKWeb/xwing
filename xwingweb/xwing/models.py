from django.db import models

# Create your models here.

class Boite(models.Model):
    nom = models.CharField(maxlength=50)
    image = models.CharField(maxlength=50)


class Carte(models.Model):
    nom = models.CharField(maxlength=50)
    points = models.IntegerField()
    boite = models.ForeignKey(Boite)

class Meta:
    abstract = True

class Amelioration(Carte):
    AMELIORATION_CHOICES = (
        ('TP', 'Torpille'),
        ('DR', 'Droide'),
        ('TR', 'Tourelle'),
        ('MD', 'Medailles'),
        ('MS', 'Missiles'),
    )
    type_amelioration = models.CharField(max_length=2, choices=AMELIORATION_CHOICES)

              
class Pilote(Carte):
    type_vaisseau = models.ForeignKey(Vaisseau)

class Ameliorations_Pilote(Carte):
     pilote =  models.ForeignKey(Pilote)
     nombre = models.IntegerField()
     type_amelioration = models.ForeignKey(Amelioration)

class Vaisseau(models.Model):
    VAISSEAU_CHOICES = (
        ('XW', 'XWing'),
        ('YW', 'YWing'),
        ('TF', 'Chasseau TIE'),
        ('TA', 'TIE Advance'),
    )
    type_vaisseau = models.CharField(max_length=2, choices=VAISSEAU_CHOICES)
