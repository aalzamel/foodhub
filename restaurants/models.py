from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	logo = models.ImageField(null=True, blank=True, upload_to="restaurant_images")

	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ["name"]	

	def get_absolute_url(self):
		return reverse("restaurant_detail", kwargs={"restaurant_id":self.id})