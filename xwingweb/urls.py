from django.conf.urls import patterns, include, url
from xwing.views import *
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='xwing/')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^xwing/', include('xwing.index')),
    # Examples:
    # url(r'^$', 'xwingweb.views.home', name='home'),
    # url(r'^xwingweb/', include('xwingweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
