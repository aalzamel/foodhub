from django import forms
from .models import Restaurant, Item
from django.contrib.auth.models import User


class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = '__all__'
		exclude = ['slug']
		widgets = {
			'opening_time' : forms.TimeInput(attrs={'type':'time'}),
			'closing_time' : forms.TimeInput(attrs={'type':'time'}),
		}


class ItemForm(forms.ModelForm):
	class Meta :
		model = Item
		fields = ['restaurant', 'name', 'description', 'price', 'active']


class UserSignUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		widgets = {
			'password': forms.PasswordInput(),
		}

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())