from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration_authentication import views as registration_authentication_views
from storefront import views as storefront_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', registration_authentication_views.landing),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tests/$', registration_authentication_views.qunit_tests),
    url(r'^placeholder/$', registration_authentication_views.placeholder),
    url(r'^error/$', registration_authentication_views.error_page),
    url(r'^register/$', registration_authentication_views.register),
    url(r'^login/$', registration_authentication_views.user_login, name='login'),
    url(r'^logout/$', registration_authentication_views.user_logout, name='logout'),
    url(r'^storefront/$', storefront_views.storefront_main, name= 'storefront_main')
)
urlpatterns += staticfiles_urlpatterns()