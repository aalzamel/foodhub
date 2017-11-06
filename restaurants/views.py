from django.shortcuts import render, get_object_or_404
from .models import Restaurant

# Create your views here.
def restaurant_list(request):
	objects = Restaurant.objects.all()
	context = {
	"objects_list": objects

	}

	return render(request, "restaurant_list.html", context)

def restaurant_detail(request, restaurant_id):
	rest_item = get_object_or_404(Restaurant, id=restaurant_id)
	context = {
	"item": rest_item
	}
	return render(request, "restaurant_detail.html", context)