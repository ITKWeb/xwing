# Create your views here.
from django.http import HttpResponse
from django.db.models import Boite

def index(request):
    return HttpResponse('<h1>Hello world</h1>')
	


urlpatterns = patterns('',
    url(r'^$', 'person.views.index'),
    url(r'^profile/$', TemplateView.as_view(template_name='profile.html')),
)


