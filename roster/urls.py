# app urls roster/urls.py

from django.conf.urls.defaults import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='roster_home'),
    
    url(r'^teamRoster/$', views.teamRoster, name='roster_teamRoster'),
    
    url(r'^players/(?P<pk>\d+)$', views.players, name='roster_Player'),
       
)