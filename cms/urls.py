from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
                       url(r'^visitor/$', views.visitor_list, name='visitor_list'),
                       url(r'^visitor/add/$', views.visitor_edit, name='visitor_add'),
                       url(r'^visitor/mod/(?P<visitor_id>\d+)/$', views.visitor_edit, name='visitor_mod'),
                       url(r'^visitor/del/(?P<visitor_id>\d+)/$', views.visitor_del, name='visitor_del'),

                       url(r'^log/(?P<visitor_id>\d+)/$', views.LogList.as_view(), name='log_list'),
                       url(r'^log/add/(?P<visitor_id>\d+)/$', views.log_edit, name='log_add'),
                       url(r'^log/mod/(?P<visitor_id>\d+)/(?P<log_id>\d+)/$', views.log_edit,
                           name='log_mod'),
                       url(r'^log/del/(?P<visitor_id>\d+)/(?P<log_id>\d+)/$', views.log_del,
                           name='log_del'),
                       )
