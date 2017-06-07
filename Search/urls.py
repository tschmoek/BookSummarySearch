from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^search$', views.search, name='search'),

	# url(r'^get_name$', views.get_name, name='get_name'),

	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
	url(r'^searchQuery/(?P<query>[a-zA-Z0-9\s]*$)', views.searchQuery, name='searchQuery'),

	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()