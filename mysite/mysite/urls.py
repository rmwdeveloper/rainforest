from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration_authentication import views as registration_authentication_views
from portfolio_listing import views as portfolio_listing_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', registration_authentication_views.landing , name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', registration_authentication_views.register, name='register'),
    url(r'^login/$', registration_authentication_views.user_login, name='login'),
    url(r'^logout/$', registration_authentication_views.user_logout, name='logout'),
    url(r'^portfolio/$', portfolio_listing_views.portfolio , name= 'portfolio'),
    (r'^contact/', include('contact_form.urls')),
) + static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns() 