
def homepage(request):    
	return True
	
# module = nom du module (sondages, pour nous)
# Boite  = définition d'un modèle (Boite)
from django.shortcuts import render_to_response
from modeles.models import Boite
    list_boites = Boite.objects.all()         
	return render_to_response('templates/index.html', { 'list_boites': list_boites })