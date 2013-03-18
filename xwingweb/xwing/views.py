# Create your views here.
from django.shortcuts import render_to_response
from xwingweb.xwing.models import Boite

def index_3(request):    
    list_boites = Boite.objects.all()         
    return render_to_response('index.html', { 'list_boites': list_boites })
