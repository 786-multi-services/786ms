from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$',views.std_login,name="std_login"),
	url(r'^signout/$',views.signout,name="logout"),
	url(r'^register/$',views.std_register,name="std_register"),
	url(r'^details/$',views.std_details,name="std_details"),
	url(r'^manager/$',views.manager_login,name="manager_login"),
	url(r'^manager/manager-panel/$',views.manager_panel,name="manager_panel"),
	url(r'^manager/manager-panel/student/(?P<pk>[0-9]+)/$',views.view_std,name="view_std"),
]
