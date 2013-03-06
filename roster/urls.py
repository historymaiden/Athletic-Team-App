# app urls roster/urls.py

from django.conf.urls.defaults import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='roster_home'),
    
    url(r'^teamRoster/(?P<pk>\d+)/$', 'roster.views.teamRoster', name='roster_teamRoster'),
    
    url(r'^players/(?P<pk>\d+)$', views.players, name='roster_Player'),
     
    # Uncomment the admin/doc line below to enable admin documentation:
   # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),  
)