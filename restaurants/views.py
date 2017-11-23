from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Item
from .forms import RestaurantForm, ItemForm, UserSignUp, UserLogin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q
import datetime
from django.http import Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def usersignup(request):
	context = {}
	form = UserSignUp()
	context['form'] = form

	if request.method == "POST":
		form = UserSignUp(request.POST)
		if form.is_valid():
			user = form.save()
			username = user.username
			password = user.password
			user.set_password(password)
			user.save()
			auth = authenticate(username=username, password=password)
			login(request, auth)
			messages.success(request,"You have successfuly signed up")
			return redirect('restaurant_list')
		messages.warning(request, form.errors)
		return redirect('usersignup')
	return render(request,"signup.html", context)



def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form

	if request.method == "POST":
		form = UserLogin(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth = authenticate(username=username, password=password)
			if auth is not None:
				login(request, auth)
				messages.success(request,"You have successfuly signed up")
				return redirect('restaurant_list')
			messages.warning(request, "username and password combination incorrect")
			return redirect('userlogin')
		messages.warning(request, form.errors)
		return redirect('userlogin')
	return render(request,"login.html", context)



def userlogout(request):
	logout(request)
	return redirect("userlogin")



# Create your views here.
def restaurant_list(request):


	objects = Restaurant.objects.all()



	query = request.GET.get('q')
	if query:
		objects = objects.filter(
		Q(name__icontains=query)
		).distinct()


	paginator = Paginator(objects, 1) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	context = {
		"restaurant_list": objects

	}

	return render(request, "restaurant_list.html", context)

def restaurant_detail(request, restaurant_slug):

	now = timezone.now().time()
	# opening_time = Restaurant.objects.get(opening_time=restaurant_slug)
	# closing_time = Restaurant.objects.get(closing_time=restaurant_slug)

	# # if opening_time > now < closing_time:
	# # 	rest_status = "open"
	# # rest_status = "close"
	# # print(rest_status)

	# print(now)
	# print(opening_time)
	# print(closing_time)

	if request.user.is_staff:
		menu_items = Item.objects.filter(restaurant__slug=restaurant_slug)
	else:
		menu_items = Item.objects.filter(restaurant__slug=restaurant_slug, active=True)
	

	rest_item = get_object_or_404(Restaurant, slug=restaurant_slug)
	context = {
		"item": rest_item,
		"menu_items": menu_items,
		"now": now,
		# "opening_time": opening_time,
		# "closing_time": closing_time,
		# "rest_status": rest_status
	}
	return render(request, "restaurant_detail.html", context)

def restaurant_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404

	form = RestaurantForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")
	context = {
		"form": form,

	}
	return render(request, "restaurant_create.html", context)



def restaurant_update(request, restaurant_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	item = Restaurant.objects.get(slug=restaurant_slug)
	form = RestaurantForm(request.POST or None, request.FILES or None, instance=item)
	if form.is_valid():
		form.save()
		return redirect("restaurant_detail", restaurant_slug=item.slug)
	context = {
		"form": form,
		"item": item,

	}
	return render(request, "restaurant_update.html", context)


def restaurant_delete(request, restaurant_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404	
	Restaurant.objects.get(slug=restaurant_slug).delete()
	return redirect("restaurant_list")


def item_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = ItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")

	context = {
			"form": form,

		}

	return render(request, "item_create.html", context)



def item_update(request, item_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	itemx = Item.objects.get(slug=item_slug)
	form = ItemForm(request.POST or None, instance=item_slug)

	if form.is_valid():
		form.save()
	return redirect("restaurant_list")

	context = {
			"form": form,
			"itemx": itemx,

		}

	return render(request, "item_update.html", context)

def item_delete(request, item_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	Item.objects.get(slug=item_slug).delete()
	return redirect("restaurant_list")
