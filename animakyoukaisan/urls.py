from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('django.contrib.auth.urls')),

    url(r'^update/$',   'profiling.views.index_page',           name='index_page'),
    url(r'^register/$', 'profiling.views.registration_page',    name='registration_page'),
    url(r'^login/$',    'profiling.views.login_page',           name='login_page'),
    url(r'^logout/$',   'profiling.views.logout_page',          name='logout_page'),
    url(r'^forgot/$',   'profiling.views.reset_password_page',  name='reset_password_page'),

    url(r'^tinymce/',           include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^$', lambda x: HttpResponseRedirect('/update/'), name='home_page'),
)
