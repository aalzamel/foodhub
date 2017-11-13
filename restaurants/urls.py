from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^list/$', views.restaurant_list, name="restaurant_list"),
	url(r'^detail/(?P<restaurant_id>\d+)/$', views.restaurant_detail, name="restaurant_detail"),
    url(r'^restaurant_create/$', views.restaurant_create, name="restaurant_create"),
	url(r'^restaurant_update/(?P<restaurant_id>\d+)/$', views.restaurant_update, name="restaurant_update"),
	url(r'^restaurant_delete/(?P<restaurant_id>\d+)/$', views.restaurant_delete, name="restaurant_delete"),


]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)