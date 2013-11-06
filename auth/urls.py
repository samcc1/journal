from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('auth.views',
	url(r'^login',	'login'),
	url(r'^logout',	'logout'),
	url(r'^newUser',	'newUser'),
)
