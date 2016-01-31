from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scienceweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(pattern_name='home2', permanent=False),name='home'),                    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', 'django.contrib.auth.views.login',{'template_name':'home.html'}, name='home2'),                
    url(r'^accounts/logout', 'django.contrib.auth.views.logout',{'next_page':'../home'}, name='logout'),
    #url(r'^accounts/resetpassword', views.sendPassword),
    url(r'^users/', include('users.urls')),
    url(r'^groups/', include('users.urls')),



)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)