from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^list/$', views.restaurant_list, name="restaurat_list"),
	url(r'^detail/(?P<restaurant_id>\d+)/$', views.restaurant_detail, name="restaurant_detail"),
]
