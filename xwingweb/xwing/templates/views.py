
def homepage(request):    
	return True
	
# module = nom du module (sondages, pour nous)
# Boite  = d�finition d'un mod�le (Boite)
from django.shortcuts import render_to_response
from xwingweb.models import Boite
    list_boites = Boite.objects.all()         
	return render_to_response('index.html', { 'list_boites': list_boites })