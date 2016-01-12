from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from users import views
from django.contrib.auth import views as auth_views
import django_messages.views


urlpatterns = patterns('',
#     url(r'^$', views.HomePageView.as_view(), name='editor_home' ),
#     url(r'^login$', 
#         auth_views.login,
#         {'template_name': 'registration/login_reviewer.html'},
#         name='editor_login'
#     ),
#     url(r'^logout$', RedirectView.as_view(url='/accounts/logout', permanent=False), name='editor_logout' ),
#     url(r'^edit$', views.edit, name='editor_edit' ),
#     url(r'^register$', views.enviarPeticion, name="editor_register" ),
#     url(r'^activate/(?P<token>.*)/$', views.activar, name="editor_activate" ),
)





urlpatterns += patterns('',
                        url(r'^messages/inbox/$', django_messages.views.inbox, {'template_name': 'inbox/my_inbox.html',},name='editor_messages_inbox'),
                        url(r'^messages/compose/$', django_messages.views.compose, {'template_name': 'inbox/my_compose.html',},name='editor_messages_compose'),
                        url(r'^messages/outbox/$', django_messages.views.outbox, {'template_name': 'inbox/my_outbox.html',},name='editor_messages_outbox'),
                        url(r'^messages/trash/$', django_messages.views.trash, {'template_name': 'inbox/my_trash.html',},name='editor_messages_trash'),
                        url(r'^messages/view/(?P<message_id>[\d]+)/$', django_messages.views.view, {'template_name': 'inbox/my_view.html',},name='editor_messages_view'),
                        url(r'^messages/', include('django_messages.urls')),
                        )