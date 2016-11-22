from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /jobApp/
    url(r'^$', views.index, name='index'),
    
    #ex: /jobApp/3/
    url(r'^(?P<job_id>[0-9]+)/$', views.details, name='details'),

    #url /jobApp?3/results/
    url(r'^(?P<job_id>[0-9]+)/results/$', views.results, name='results'),
]