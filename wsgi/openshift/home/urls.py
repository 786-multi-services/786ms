from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views
from django.conf.urls import handler404, handler500

handler404 = views.index
urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^#(>P<tag>[a-z])/$',views.index,name="index"),
]
