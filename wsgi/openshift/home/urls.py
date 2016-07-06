from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'#(?P<tag>[a-z]+)/$',views.index,name="index"),
]
