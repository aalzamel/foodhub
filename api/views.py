from django.shortcuts import render
from restaurants.models import Restaurant
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer, RestaurantCreateUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter


# Create your views here.
class RestaurantListAPIView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	permission_classes = [AllowAny,]
	filter_backends = [SearchFilter,]
	search_fields = ['name', 'description']


class RestaurantDetailAPIView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	permission_classes = [IsAuthenticated,]
	lookup_field = 'slug'
	lookup_url_kwarg = 'restaurant_slug'

class RestaurantDeleteAPIView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	permission_classes = [IsAuthenticated, IsAdminUser,]
	lookup_field = 'slug'
	lookup_url_kwarg = 'restaurant_slug'

class RestaurantCreateAPIView(CreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateUpdateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]
	


class RestaurantUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateUpdateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]
	lookup_field = 'slug'
	lookup_url_kwarg = 'restaurant_slug'
	