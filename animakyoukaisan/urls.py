from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', lambda x: HttpResponseRedirect('/admin/')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
