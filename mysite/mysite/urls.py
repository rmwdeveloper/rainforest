from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration_authentication import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', views.landing),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tests/$', views.qunit_tests),
    url(r'^placeholder/$', views.placeholder),
    url(r'^error/$', views.error_page),
    url(r'^register/$', views.register),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout')
)
urlpatterns += staticfiles_urlpatterns()