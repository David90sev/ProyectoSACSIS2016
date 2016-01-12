from django.conf.urls import patterns, include, url

from django.contrib import admin
import users
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scienceweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', 'django.contrib.auth.views.login',{'template_name':'index.html'}, name='login'),                        
    url(r'^accounts/logout', 'django.contrib.auth.views.logout',{'next_page':'../home'}, name='logout'),
    #url(r'^accounts/resetpassword', views.sendPassword),
#     url(r'^accounts/', include(users.urls),

)