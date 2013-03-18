from sondages.models import *

class Choix:
   def __init__(self, boite, quantite):
       self.boite = boite
       self.quantite = quantite
   def presenter(self) :
       return self.quantite + " " + self.boite

def get_random(max_points, liste_choix, nb_joueurs, camp):
    for element in liste_choix :
        liste_vaisseau=get_liste_vaisseau_reb(liste_choix, camp)
        liste_pilote=get_liste_pilote_reb(liste_choix, camp)
        liste_amelio=get_liste_amelio_reb(liste_choix, camp)
        
    return liste_

def get_liste_vaisseau_reb(liste_choix, camp):
    return liste_

def get_liste_pilote_reb(liste_choix, camp):
    return liste_

def get_liste_pilote_reb(liste_choix, camp):
    return liste_
