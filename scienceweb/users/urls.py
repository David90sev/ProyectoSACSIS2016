from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from users import views
from django.contrib.auth import views as auth_views
import django_messages.views


urlpatterns = patterns('',
                       url(r'^profile', views.view_profile),
                       url(r'^register$', views.registration_choose),
                       url(r'^register_yi', views.registration_young_inv),
                       url(r'^register_pi', views.registration_principal_inv),
                       url(r'^register/activate/(?P<token>.*)$', views.activate, name="activate" ),
)





urlpatterns += patterns('',
                        url(r'^messages/inbox/$', django_messages.views.inbox, {'template_name': 'inbox/my_inbox.html',},name='editor_messages_inbox'),
                        url(r'^messages/compose/$', django_messages.views.compose, {'template_name': 'inbox/my_compose.html',},name='editor_messages_compose'),
                        url(r'^messages/outbox/$', django_messages.views.outbox, {'template_name': 'inbox/my_outbox.html',},name='editor_messages_outbox'),
                        url(r'^messages/trash/$', django_messages.views.trash, {'template_name': 'inbox/my_trash.html',},name='editor_messages_trash'),
                        url(r'^messages/view/(?P<message_id>[\d]+)/$', django_messages.views.view, {'template_name': 'inbox/my_view.html',},name='editor_messages_view'),
                        url(r'^messages/', include('django_messages.urls')),
                        )