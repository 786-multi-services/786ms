from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
	url(r'^',include('home.urls')),
	url(r'^career/',include('career.urls')),
    url(r'^student/',include('students.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_URL)
