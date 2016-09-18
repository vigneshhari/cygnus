from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from . import views



urlpatterns = patterns('',
    url(r'^app/', include('accounts.urls')),
    url(r'^quiz/', include('quizpage.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
 (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
 )
