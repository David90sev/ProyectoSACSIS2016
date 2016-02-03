from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from users import views
from django.contrib.auth import views as auth_views
import django_messages.views


urlpatterns = patterns('',
                       url(r'^dashboard',views.dashboard, name="dashboard"),
                       url(r'^profile$', views.view_profile, name="self_profile"),
                       url(r'^profile/(?P<userId>.*)$', views.view_profile_withId, name="user_profile_withId"),
                       url(r'^search', views.search_user),
                       url(r'^register$', views.registration_choose),
                       url(r'^register_yi', views.registration_young_inv),
                       url(r'^register_pi', views.registration_principal_inv),
                       url(r'^register/activate/(?P<token>.*)$', views.activate, name="activate" ),
)

urlpatterns += patterns('',
    url(r'^list',views.list_investigation_groups, name='group_list'),
    url(r'^show/(?P<groupId>\d*)$',views.group_view, name='group_show'),
    url(r'^create$',views.group_create, name="group_create"),
    url(r'^addparticipant/(?P<groupId>\d*)$',views.add_participant, name="group_add_participant"),
    url(r'^keyremove/young/(?P<users_id>\d*)/(?P<word_word>.*)', views.remove_keyword_from_profile, {'is_young':'1',},name="keyremove"),
    url(r'^keyremove/principal/(?P<users_id>\d*)/(?P<word_word>.*)', views.remove_keyword_from_profile, {'is_young':'0',},name="keyremove"),
    url(r'offers/add',views.add_offer, name='add_offers'),
    url(r'offers/list',views.list_my_offers, name="list_offers"),
    url(r'^offers/view/(?P<offer_id>.*)',views.view_offer, name="view_offer"),
                        )


urlpatterns += patterns('',
                        url(r'^messages/inbox/$', django_messages.views.inbox, {'template_name': 'inbox/my_inbox.html',},name='editor_messages_inbox'),
                        url(r'^messages/compose/$', django_messages.views.compose, {'template_name': 'inbox/my_compose.html'},name='editor_messages_compose'),
                        url(r'^messages/outbox/$', django_messages.views.outbox, {'template_name': 'inbox/my_outbox.html',},name='editor_messages_outbox'),
                        url(r'^messages/trash/$', django_messages.views.trash, {'template_name': 'inbox/my_trash.html',},name='editor_messages_trash'),
                        url(r'^messages/view/(?P<message_id>[\d]+)/$', django_messages.views.view, {'template_name': 'inbox/my_view.html',},name='editor_messages_view'),
                        url(r'^messages/', include('django_messages.urls')),
                        )