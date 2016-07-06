from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'
handler403 = 'home.views.handler403'
handler400 = 'home.views.handler400'

urlpatterns = [
	url(r'',include('home.urls')),
	# url(r'career/',include('career.urls')),
    # url(r'student/',include('students.urls')),
	# url(r'shops/', include('shops.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_URL)
