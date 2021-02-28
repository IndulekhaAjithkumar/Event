from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	time = models.CharField(max_length=255)
	date = models.CharField(max_length=255, default="Events")
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	location = models.TextField()
	#time = models.CharField(max_length=255)

	def __str__(self):
		return self.time + ' | ' + str(self.name)

	def get_absolute_url(self):
		#return reverse('article-detail',args=(str(self.id)))
		return reverse('home',args=(str(self.id)))
		fields = ('title','body')