from django.db import models

# Create your models here.
class profile(models.Model):
	"""docstring for Profile"""
	name = models.CharField(max_length=1200)
	description = models.TextField(default='description default')

	def __unicode__(self):
		return self.name

