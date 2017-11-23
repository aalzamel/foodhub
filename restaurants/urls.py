from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^list/$', views.restaurant_list, name="restaurant_list"),
	url(r'^detail/(?P<restaurant_slug>[-\w]+)/$', views.restaurant_detail, name="restaurant_detail"),
    url(r'^restaurant_create/$', views.restaurant_create, name="restaurant_create"),
	url(r'^restaurant_update/(?P<restaurant_slug>[-\w]+)/$', views.restaurant_update, name="restaurant_update"),
	url(r'^restaurant_delete/(?P<restaurant_slug>[-\w]+)/$', views.restaurant_delete, name="restaurant_delete"),
	url(r'^item_delete/(?P<item_slug>[-\w]+)/$', views.item_delete, name="item_delete"),
	url(r'^item_update/(?P<item_slug>[-\w]+)/$', views.item_update, name="item_update"),
    url(r'^item_create/$', views.item_create, name="item_create"),
    url(r'^signup/$', views.usersignup, name="usersignup"),
    url(r'^login/$', views.userlogin, name="userlogin"),

    url(r'^logout/$', views.userlogout, name="userlogout"),



]
