from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(blank=True)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	logo = models.ImageField(null=True, blank=True, upload_to="restaurant_images")

	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ["name"]	

	def get_absolute_url(self):
		return reverse("restaurant_detail", kwargs={"restaurant_slug":self.slug})


def create_slug(instance, new_slug=None):
	slug_value = slugify(instance.name)
	if new_slug is not None:
		slug_value = new_slug
		query = Restaurant.objects.filter(slug=slug_value)
		print(query)
		if query.exists():
			slug_value = "%s-%s"%(slug_value, query.last().id)
			return create_slug(instance, new_slug=slug_value)
	return slug_value


def pre_save_post_receiver(*args, **kwargs):
	instance = kwargs['instance']
	if instance.slug:
		x = slugify(instance.name)
		instance.slug = create_slug(instance, new_slug=x)
	if not instance.slug:
		instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Restaurant)



class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	name = models.CharField(max_length=150, unique=True)
	slug = models.SlugField(blank=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name




def pre_save_post_receiver1(*args, **kwargs):
	instance = kwargs['instance']
	if instance.slug:
		x = slugify(instance.name)
		instance.slug = create_slug(instance, new_slug=x)
	if not instance.slug:
		instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver1, sender=Item)
