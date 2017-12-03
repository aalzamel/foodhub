from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.RestaurantListAPIView.as_view(), name="list"),
    url(r'^create/$', views.RestaurantCreateAPIView.as_view(), name="create"),
    url(r'^(?P<restaurant_slug>[-\w]+)/$', views.RestaurantDetailAPIView.as_view(), name="detail"),
	url(r'^(?P<restaurant_slug>[-\w]+)/delete/$', views.RestaurantDeleteAPIView.as_view(), name="delete"),
	url(r'^(?P<restaurant_slug>[-\w]+)/update/$', views.RestaurantUpdateAPIView.as_view(), name="update"),
]

