from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$',views.std_login,name="std_login"),
	url(r'^signout/$',views.signout,name="logout"),
	url(r'^register/$',views.std_register,name="std_register"),
	url(r'^manager/$',views.manager_login,name="manager_login"),
]
